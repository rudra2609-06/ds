# used to split py or markdown code similar to RecursiveCharacterTextSplitting but now seperators are diff

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

splitter = RecursiveCharacterTextSplitter.from_language(
	# there are many options like MARKDOWN and other lang in LANGUAGE
	language=Language.PYTHON,
	chunk_size = 400,
	chunk_overlap = 0
)

text = """
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
"""

chunks = splitter.split_text(text)
# print(len(chunks))
print(chunks[0])