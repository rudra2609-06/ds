from langchain_core.runnables import RunnableSequence, RunnableParallel
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
	template='Generate 5 Pointer Summary on topic. \n {topic}',
	input_variables=['topic']
)

prompt2 = PromptTemplate(
	template='Generate 2 Imp Interview Questions on topic. \n {topic}',
	input_variables=['topic']
)

chain = RunnableParallel({
	'summary' : RunnableSequence(prompt1,model1,parser),
	'questions' : RunnableSequence(prompt2,model2,parser)
})

res = chain.invoke({'topic' : 'LinearRegression'})

print(res)

chain.get_graph().print_ascii()


