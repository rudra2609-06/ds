from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv
import os

load_dotenv()


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

# here, in Chroma Db Collection name means Table name w.r.t to RDBMS
vector_store = Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview"),
    collection_name="first-demo",
    persist_directory="./chroma_db",
)

# add documents 

# after adding it gives id to each doc
vector_store.add_documents(docs)

vector_store.get(include=['embeddings','documents','metadatas'])


# search documents

res = vector_store.similarity_search(query='who among this is leader of team',k=1)
res = vector_store.similarity_search_with_score(query='who among this is leader of team',k=1)

# metadata filtering
res = vector_store.similarity_search_with_score(query='',k=1,filter={'team':'Mumbai Indians'})

print(res)

