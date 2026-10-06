from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
	repo_id='meta-llama/Llama-3.1-8B-Instruct',
	task= 'text-generation'
)

model = ChatHuggingFace(
	llm = llm	
)

class Person(BaseModel):
	name : str = Field(...,description='Name of the person')
	age : int  = Field(...,gt=18,description='Age of the person')
	city : str = Field(...,description='city name where person resides')

parser = PydanticOutputParser(pydantic_object=Person)

t1 = PromptTemplate(
	template='Generate name, age and city of person within {place} \n {format_instruction} follow instructions strictly please only provide me fields that have asked no extra explainatin',
	input_variables=['place'],
	partial_variables={'format_instruction' : parser.get_format_instructions()}
)

p1 = t1.invoke({'place' : 'india'})

# res = model.invoke(p1)
# print(res.content)
# final_res = parser.parse(res.content)

# print(final_res)


# -------------------- using chain --------------------

chain = t1 | model | parser

res = chain.invoke({'place' : 'india'})

print(res)