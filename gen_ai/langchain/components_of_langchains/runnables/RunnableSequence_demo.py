from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
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

prompt = PromptTemplate(
	template='Generate 5 pointer Summary for the topic. \n {topic}',
	input_variables=['topic']
)

parser = StrOutputParser()


chain = RunnableSequence(prompt,model1,parser)
# ----------- OR via LCEL ----------------
# chain = prompt | model1 | parser

res = chain.invoke({'topic' : 'LinearRegression'})

print(res)


