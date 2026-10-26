# allows you to fetch the similar document from vector store or vectro db by doing semantic searching

# The vector store does the actual semantic search. The retriever is a thin wrapper that gives it a standard interface so chains can call it.
# %%
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
import os

doc1 = Document(
    page_content="Virat Kohli is an Indian international cricketer known for his aggressive batting style and consistency. He is a top-order batsman who has represented India in all formats of cricket.",
    metadata={"team": "Royal Challengers Bengaluru"},
)

doc2 = Document(
    page_content="Rohit Sharma is an Indian international cricketer known for his elegant batting and leadership skills. He is a right-handed opening batsman and has captained India in international cricket.",
    metadata={"team": "Mumbai Indians"},
)

doc3 = Document(
    page_content="MS Dhoni is a former Indian international captain and wicketkeeper-batsman known for his finishing ability and calm leadership. He has played a major role in Chennai Super Kings' success in the IPL.",
    metadata={"team": "Chennai Super Kings"},
)

docs = [doc1, doc2, doc3]


embedding_model = GoogleGenerativeAIEmbeddings(
    api_key=os.environ.get("GEMINI_API_KEY"), model="gemini-embedding-2-preview"
)

vector_store = Chroma(
	embedding_function=embedding_model,
	collection_name='my_collection',
)

vector_store.add_documents(docs)

# convert vector store to retrievers

retriever = vector_store.as_retriever(search_kwargs={'k' : 1})

query = 'about captain cool'

results = retriever.invoke(query)