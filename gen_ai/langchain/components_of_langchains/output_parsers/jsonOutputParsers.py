# it enforces llm to send res in json form
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
	repo_id='meta-llama/Llama-3.1-8B-Instruct',
	task= 'text-generation'
)

model = ChatHuggingFace(
	llm = llm	
)

parser = JsonOutputParser()


# why it is known as partial_variables -> as it is not filled using RunTime it is filled before the RunTime

# what's the diff b/w input_variables and partial_variables
# input_variables -> filled during run time
# partial_variables -> filled before run time by langchain fn get_format_instructions

t1 = PromptTemplate(
	template = 'Give me a the name, age of pm of india {format_instruction}',
	input_variables=[],
	partial_variables={'format_instruction' : parser.get_format_instructions()}
)

# p1 = t1.format()

# res  = model.invoke(p1)
# print(parser.parse(res.content))


# ---------------------------- using chains easier way ------------------------

chain = t1 | model | parser

# if we have no input var to send send empty {}
res = chain.invoke({})

print(res)


