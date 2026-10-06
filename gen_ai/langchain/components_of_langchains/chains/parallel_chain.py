from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


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
	template='Generate 10 Pointer Summary from the provided {text} such that it should be simple and sufficient enough to understand',
	input_variables=['text']
)

prompt2 = PromptTemplate(
	template='Pick Top 3 freqently used words from {text}.\n Output format:- Word -> Count',
	input_variables=['text']
)

prompt3 = PromptTemplate(
	template='Merge This 2 things such that first comes Summary and then freqently used words. \n {notes} and {freq}',
	input_variables=['notes','freq']
)



parallel_chains = RunnableParallel({
	'notes': prompt1 | model1 | parser,
	'freq' : prompt2 | model2 | parser
})


text = """
Linear regression is a fundamental supervised machine learning algorithm that models the linear relationship between a dependent variable and one or more independent variables.  It predicts continuous values by fitting a straight line through data points, minimizing the error between observed and predicted values using methods like Ordinary Least Squares (OLS).  This technique is widely used for forecasting and understanding variable dependencies
"""

merging_chain = prompt3 | model2 | parser

final_chain = parallel_chains | merging_chain

res = final_chain.invoke({'text' : text})

print(res)

final_chain.get_graph().print_ascii()