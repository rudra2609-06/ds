"""
sometimes our query is ambigous enough that it can't capture meaning from the diverse docs.

For eg, our data source has every information related to health, nutrition, exercise, etc.
Now we just pass a query: how to stay healthy ?
It has many meanings:- 
1.What to eat to stay healthy
2.How often to exercise to stay healthy
3.How can i manage stress to stay healthy 

So what it does it:
It takes input query 
Passes to an LLM that generate multiple querys
Performs retrival for each sub-query
combines and de-duplicates the result
"""
# %%
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

docs = [
    # Walking
    Document(page_content="Adults who walk briskly for about 30 minutes a day, five days a week, meet a large part of the weekly activity guideline and show better heart health.", metadata={"topic": "walking"}),
    Document(page_content="Studies link roughly 7,000 to 8,000 steps per day with a noticeably lower risk of early death compared to very low step counts. Benefits level off at higher counts.", metadata={"topic": "walking"}),
    Document(page_content="Breaking walking into three 10-minute walks after meals helps lower blood sugar spikes and is easier to fit into a busy day.", metadata={"topic": "walking"}),

    # Exercise
    Document(page_content="Health guidelines recommend 150 to 300 minutes of moderate aerobic activity per week, or 75 to 150 minutes of vigorous activity, for adults.", metadata={"topic": "exercise"}),
    Document(page_content="Muscle-strengthening exercises such as squats, push-ups and resistance bands should be done at least two days per week, covering all major muscle groups.", metadata={"topic": "exercise"}),
    Document(page_content="Rest days and 7 to 9 hours of sleep let muscles repair and reduce injury risk. Overtraining without recovery can lower performance and immunity.", metadata={"topic": "exercise"}),

    # Supplements
    Document(page_content="Creatine monohydrate at 3 to 5 grams per day is one of the most researched supplements for improving strength and high-intensity exercise performance.", metadata={"topic": "supplements"}),
    Document(page_content="Active adults often aim for 1.2 to 2.0 grams of protein per kilogram of body weight daily. Whey protein powder is a convenient way to reach the target.", metadata={"topic": "supplements"}),
    Document(page_content="Vitamin D supplements may help people with low sun exposure or a diagnosed deficiency. Taking more than needed does not improve fitness and can be harmful.", metadata={"topic": "supplements"}),
    Document(page_content="Most healthy people who eat a balanced diet do not need multivitamins. Supplements should support the diet, not replace it, and should be discussed with a doctor.", metadata={"topic": "supplements"}),
    Document(
        page_content="Getting 10 to 30 minutes of midday sunlight on bare arms and legs a few times a week helps the skin make vitamin D. People with darker skin or those living far from the equator may need longer exposure.",
        metadata={"topic": "solar"},
    ),
    Document(
        page_content="Too much sun exposure raises the risk of sunburn, premature skin aging and skin cancer. Use broad-spectrum sunscreen of SPF 30 or higher, wear a hat and sunglasses, and avoid the strongest sun between 10 AM and 4 PM.",
        metadata={"topic": "solar"},
    )
]



embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector_store = Chroma.from_documents(docs, embeddings)

model = ChatGoogleGenerativeAI(
	model='gemini-2.5-flash'
)


retriever = vector_store.as_retriever(search_type='similarity',search_kwargs = {'k' : 2})

multi_query_retriever = MultiQueryRetriever.from_llm(
	llm=model,
	retriever=retriever
)

query = 'How to remain healthy'

simple_retriever_res = multi_query_retriever.invoke(query)
multi_query_retriever_res = multi_query_retriever.invoke(query)