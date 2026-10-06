from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


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

parser = StrOutputParser()

prompt1 = PromptTemplate(
	template='Generate joke on topic {topic}',
	input_variables=['topic']
)


prompt2 = PromptTemplate(
	template='Provide 15 words explaination of the particular joke. \n {joke}',
	input_variables=['joke']
)


joke_generator_chain = RunnableSequence(prompt1,model1,parser)

joke_explaination_generator_chain = RunnableParallel({
	'joke' : RunnablePassthrough(),
	'explaination' : RunnableSequence(prompt2,model2,parser)
})

final_chain = joke_generator_chain | joke_explaination_generator_chain

res = final_chain.invoke({'topic' : 'cricket'})

print(res)