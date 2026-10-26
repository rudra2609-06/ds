from langchain_community.document_loaders import TextLoader

loader = TextLoader(
	file_path= 'D:\ds\gen_ai\langchain\components_of_langchains\document_loaders\demo.txt',
	encoding='utf-8'
)

docs = loader.load()

print(docs[0].page_content)
