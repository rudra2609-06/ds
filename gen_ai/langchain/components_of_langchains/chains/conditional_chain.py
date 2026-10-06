from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

class ClassificationOutput(BaseModel):
	sentiment : Literal['Positive','Negative'] = Field(...,
	                                                   description='Based on the provided text you need to classify the sentiment of the user feedback into either Positive or Negative'
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

str_parser = StrOutputParser()

pydantic_parser = PydanticOutputParser(pydantic_object=ClassificationOutput)

prompt1 = PromptTemplate(
	template='Classify of the following feedback into text either positive or negative. \n {feedback} \n {formal_instructions}',
	input_variables=['feedback'],
	partial_variables={'formal_instructions' : pydantic_parser.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="""
You are a professional customer care agent.

The customer has provided feedback with the following sentiment:
{sentiment}

Respond to the customer in a warm, polite and professional manner.

For positive feedback:
- Thank the customer.
- Appreciate their feedback.
- Let them know that their satisfaction is important to us.
- Keep the response concise.
- Maximum 40 words.

Return only the customer-care response.
""",
    input_variables=["sentiment"]
)


prompt3 = PromptTemplate(
    template="""
You are a professional customer care agent.

The customer has provided feedback with the following sentiment:
{sentiment}

Respond to the customer in a polite, empathetic and professional manner.

For negative feedback:
- Acknowledge the customer's dissatisfaction.
- Apologize for the poor experience.
- Show empathy.
- Offer to help resolve the issue.
- Do not argue with or blame the customer.
- Keep the response concise.
- Maximum 40 words.

Return only the customer-care response.
""",
    input_variables=["sentiment"]
)


classifier_chain = prompt1 | model1 | pydantic_parser

# we send multiple tuples, first should be condition, what to execute
# at end default
# like if ,(else if * n), else

conditional_chain = RunnableBranch(
	(lambda x : x.sentiment == 'Positive',prompt2 | model1 | str_parser),
	(lambda x : x.sentiment == 'Negative',prompt3 | model2 | str_parser),
	RunnableLambda(lambda x : "could not find sentiment")
)

final_chain = classifier_chain | conditional_chain

res = final_chain.invoke({'feedback' : "This is the terrible Smartphone"})

print(res)



