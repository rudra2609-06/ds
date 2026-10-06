from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
	repo_id='meta-llama/Llama-3.1-8B-Instruct',
	task='text-generation',
)

model = ChatHuggingFace(
	llm=llm
)

t1 = PromptTemplate(
	template="Generate 100 words content for  {topic} such that it provides simplistic explaination to the user ",
	input_variables=['topic']
)


# p1 = t1.invoke(input('Enter the topic: '))


# res = model.invoke(p1)
# print(res.content)


# ---------------------- simple linear/Sequential chain ----------------------

parser = StrOutputParser()

chain = t1 | model | parser

res = chain.invoke({'topic' : 'KNN'})

print(res)


# chain.get_graph().print_ascii()
