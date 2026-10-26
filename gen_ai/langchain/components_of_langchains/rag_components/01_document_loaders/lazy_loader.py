from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from pathlib import Path


loader = DirectoryLoader(
	path="D:\ds\gen_ai\langchain\components_of_langchains\document_loaders",
	glob='*.pdf',
	loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

# run this file and observe that it is loading on demand one by one 
for document in docs:
	print(document.metadata) 

