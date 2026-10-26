"""
MMR (Maximal Marginal Relevance) is a search strategy that picks results that are relevant to the query but different from each other, instead of just returning the top-k most similar chunks.

The problem it solves

Plain similarity search returns the k closest vectors. If your data has near-duplicate chunks (overlapping chunks, repeated reviews, the same fact stated three ways), the top 4 results can all say the same thing. That wastes context and hides other useful information.

How MMR works

Fetch fetch_k candidates by plain similarity (default 20).
Pick the most relevant one first.
For each next pick, choose the candidate that scores best on:
relevance to the query minus similarity to the chunks already selected.
Repeat until you have k results.
"""

# %%
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

docs = [
    Document(
        page_content="Captain Cool is known for staying calm under pressure in close matches."
    ),
    Document(
        page_content="Captain Cool remains calm in pressure situations and finishes matches coolly."
    ),
    Document(page_content="Captain Cool led his team to three ICC trophies."),
    Document(
        page_content="Captain Cool is a wicketkeeper famous for lightning fast stumpings."
    ),
]

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector_store = Chroma.from_documents(docs, embeddings)

retriever = vector_store.as_retriever(
    search_type="mmr", search_kwargs={"k": 2, "lambda_mult": 0.5}
)
# if lambda_mult kept 1 mmr works as normal similarity search
# if lambda_mult kept 0 mmr gives most diverse results
# ranges b.w 0 to 1

query = "tell me about captain cool"

res = retriever.invoke(query)
