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

prompt1 = PromptTemplate(
	template="Generate 50 words report for  {topic} such that it provides simplistic explaination to the user ",
	input_variables=['topic']
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
	template='Give 5 Pointer Summary after analysing {text}',
	input_variables=['text']
)


chain = prompt1 | model | parser | prompt2 | model | parser

res = chain.invoke({'topic' : 'UnEmployement In India'})

print(res)
