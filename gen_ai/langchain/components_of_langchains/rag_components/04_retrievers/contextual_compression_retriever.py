# it is an advance retriever that improves the retrieval quality by compressing the documents after retrieval -> keeping only relavant content based on the user's query
# we use this when we want to improve the results of our rag pipelines, or we have large text with mix words

# %%
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from dotenv import load_dotenv
from langchain_classic.retrievers.document_compressors import LLMChainExtractor


docs = [
    Document(
        page_content=(
            "Our gym opens at 6 AM on weekdays and 8 AM on weekends. The locker rooms were renovated last spring "
            "and now include free towels. Members can book personal trainers at the front desk. "
            "For general health, adults should aim for 150 minutes of moderate aerobic activity per week, "
            "such as brisk walking or cycling. The cafe on the first floor sells smoothies and protein bars, "
            "and parking is free for the first two hours."
        ),
        metadata={"source": "gym_newsletter"},
    ),
    Document(
        page_content=(
            "Welcome to the community wellness blog. This month we also have a book club and a yoga workshop. "
            "Creatine monohydrate at 3 to 5 grams per day is well researched for improving strength and "
            "high-intensity performance, and it does not need a loading phase. "
            "Our next meetup is at the town library on the 14th. Please bring your own mat, and remember "
            "that the parking lot behind the library is closed for repaving."
        ),
        metadata={"source": "wellness_blog"},
    ),
    Document(
        page_content=(
            "Travel notes from my trip to Goa: the beaches were crowded, the seafood was great, and the hotel "
            "wifi was slow. One tip from a local doctor: spend 10 to 30 minutes in midday sunlight a few times "
            "a week so the skin can make vitamin D, but use SPF 30 sunscreen if you stay out longer. "
            "We also rented scooters, visited an old fort, and took a boat ride at sunset."
        ),
        metadata={"source": "travel_blog"},
    ),
    Document(
        page_content=(
            "Weekly meal prep ideas: roast vegetables on Sunday, cook a big batch of rice, and marinate chicken. "
            "Active adults often aim for 1.2 to 2.0 grams of protein per kilogram of body weight daily, "
            "and spreading it across meals helps. Store containers in the fridge for up to four days. "
            "Buy spices in bulk to save money, and label everything with the date."
        ),
        metadata={"source": "meal_prep_guide"},
    ),
    Document(
        page_content=(
            "Sleep and recovery digest. Many people scroll their phones in bed, which delays sleep. "
            "Adults need 7 to 9 hours of sleep so muscles can repair and injury risk drops. "
            "Keep the bedroom cool and dark, avoid caffeine after 3 PM, and try a consistent bedtime. "
            "Some readers also asked about new mattress brands, which we will review next week."
        ),
        metadata={"source": "sleep_digest"},
    ),
]

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector_store = Chroma.from_documents(docs, embeddings)

model = ChatGoogleGenerativeAI(
	model='gemini-2.5-flash'
)

retriever = vector_store.as_retriever(search_type='similarity',search_kwargs = {'k' : 2})
base_compressor = LLMChainExtractor.from_llm(llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash'))
contextual_compression_retriever = ContextualCompressionRetriever(
	base_compressor=base_compressor,
	base_retriever=retriever
)

query = "how much protein should active people eat?"

simple_retriever_res = retriever.invoke(query)
contextual_compression_retriever_res = contextual_compression_retriever.invoke(query)
