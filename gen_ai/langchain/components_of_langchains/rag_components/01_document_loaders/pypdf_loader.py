from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
	file_path=f'D:\ds\gen_ai\langchain\components_of_langchains\document_loaders\Essential Math for Data Science (Thomas Nield) (Z-Library).pdf',
)

docs = loader.load()

print(len(docs)) # -> 511 as there are 511 pages