from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableBranch
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal


class Sentiment(BaseModel):
	sentiment : Literal['Positive','Negative','Neutral'] = Field(...,
	                                                             description="Your Analysis of the feedback from customer should be out of this 3 variables"
																)


load_dotenv()

llm = HuggingFaceEndpoint(
	repo_id='meta-llama/Llama-3.1-8B-Instruct',
	task='text-generation',
)

model1 = ChatHuggingFace(
	llm=llm
)


model2 = ChatGoogleGenerativeAI(
	model = 'gemini-2.5-flash'
)

parser1 = StrOutputParser()

parser2 = PydanticOutputParser(pydantic_object=Sentiment)

prompt1 = PromptTemplate(
	template='You are the customer service agent expert in an e-commerce org. Your task is to understand user feedback and then classify its sentiment into either Positive, Negative or Neutral just. \n {feedback} \n {formal_instructions}',
	input_variables=['feedback'],
	partial_variables={'formal_instructions' : parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template=(
        "You are a customer service agent at an e-commerce company. "
        "The customer left POSITIVE feedback. Write a short, warm reply (3-4 sentences) "
        "that thanks them, mentions something specific from their feedback, "
        "and invites them to shop again.\n\nSentiment: {sentiment}"
    ),
    input_variables=['sentiment']
)

prompt3 = PromptTemplate(
    template=(
        "You are a customer service agent at an e-commerce company. "
        "The customer left NEGATIVE feedback. Write a polite, empathetic reply (3-5 sentences) "
        "that apologizes sincerely, acknowledges their specific problem, "
        "offers a next step (refund, replacement, or support contact), "
        "and does not make excuses or promises you cannot keep.\n\nSentiment: {sentiment}"
    ),
    input_variables=['sentiment']
)

prompt4 = PromptTemplate(
    template=(
        "You are a customer service agent at an e-commerce company. "
        "The customer left NEUTRAL feedback. Write a friendly, brief reply (2-3 sentences) "
        "that thanks them and asks one question about what would make "
        "their experience better.\n\Sentiment: {sentiment}"
    ),
    input_variables=['sentiment']
)

feedback_classification_chain = RunnableSequence(prompt1,model1,parser2)

feedback_reply_chain = RunnableBranch(
	(lambda x : x.sentiment == 'Positive', RunnableSequence(prompt2,model2,parser1)),
	(lambda x : x.sentiment == 'Negative', RunnableSequence(prompt3,model2,parser1)),
	(lambda x : x.sentiment == 'Neutral', RunnableSequence(prompt4,model2,parser1)),
	RunnableLambda(lambda x : "could not find sentiment")
)

chain = feedback_classification_chain | feedback_reply_chain

res = chain.invoke({'feedback' : "Terrible SmartPhone"})

print(res)





