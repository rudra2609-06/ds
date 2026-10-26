from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from pathlib import Path


loader = DirectoryLoader(
	path="D:\ds\gen_ai\langchain\components_of_langchains\document_loaders",
	glob='*.pdf',
	loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))