import numpy as np
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity


load_dotenv()
print('running: ')

embeddings = HuggingFaceEndpointEmbeddings(
	model='Qwen/Qwen3-Embedding-8B'
)

documents = [
	"Virat Kholi is considered as most fit cricketer in the cricket world",
	"Sachin Tendulkar is considered as God Of Cricket upon his performance",
	"Jasprit Bumrah Is Best right arm fast baller",
	"Subhman Gill is currently nominated captain of Indian Team in upcoming World Cup upon his performance while past captainship"
]

doc_embeddings = embeddings.embed_documents(documents)

query = "Tell me some thing about god of cricket"

query_embeddings = embeddings.embed_query(query)


res = cosine_similarity([query_embeddings],doc_embeddings)

print(res)

print("Best Match: ",documents[int(np.argmax(res))])

ranked = sorted(zip(documents,res[0]),key=lambda x:x[1],reverse=True)

for doc, score in ranked:
	print(f'{score} -> {doc}')