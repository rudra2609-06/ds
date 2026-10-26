# It queries wikipedia API to fetch the relevant content for given query
# %%
from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2, lang="en")

query = (
    "the geopolitical relationship between india and china w.r.t north-eastern borders"
)

docs = retriever.invoke(query)

for cnt, doc in enumerate(docs):
    print(f"{cnt + 1} -> {docs[cnt].page_content}")
