from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from sklearn.metrics.pairwise import cosine_similarity

from langchain_community.document_loaders import TextLoader
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnableParallel
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings


load_dotenv(override=True)


class ReviewAnalysis(BaseModel):
    summary: str = Field(description="A concise summary of the customer's review")
    sentiment: Literal["Positive", "Negative", "Neutral"] = Field(
        description="The review's overall sentiment"
    )


parser_pydantic = PydanticOutputParser(pydantic_object=ReviewAnalysis)
parser_str = StrOutputParser()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Resolve reviews.txt beside this script so the project can be moved.
reviews_file = Path(__file__).resolve().with_name("reviews.txt")
loader = TextLoader(file_path=str(reviews_file), encoding="utf-8")

classification_prompt = PromptTemplate(
    template=(
        "Analyze this customer review. Return a concise summary and classify its "
        "sentiment as Positive, Negative, or Neutral.\n\n"
        "Review: {review}\n\n{format_instructions}"
    ),
    input_variables=["review"],
    partial_variables={"format_instructions": parser_pydantic.get_format_instructions()},
)
classification_chain = classification_prompt | model | parser_pydantic

positive_reply_prompt = PromptTemplate(
    template=(
        "Write a warm, concise customer-service reply to this positive review. "
        "Thank the customer and refer to a specific detail.\n"
        "Review: {review}\nSummary: {summary}"
    ),
    input_variables=["review", "summary"],
)
negative_reply_prompt = PromptTemplate(
    template=(
        "Write a concise, empathetic customer-service reply to this negative review. "
        "Acknowledge the specific problem, apologize, and suggest a practical next step. "
        "Do not invent actions already taken.\nReview: {review}\nSummary: {summary}"
    ),
    input_variables=["review", "summary"],
)
neutral_reply_prompt = PromptTemplate(
    template=(
        "Write a brief, friendly customer-service reply to this neutral review. "
        "Thank the customer and ask one useful follow-up question.\n"
        "Review: {review}\nSummary: {summary}"
    ),
    input_variables=["review", "summary"],
)

reply_chain = RunnableBranch(
    (lambda x: x["sentiment"] == "Positive", positive_reply_prompt | model | parser_str),
    (lambda x: x["sentiment"] == "Negative", negative_reply_prompt | model | parser_str),
    (lambda x: x["sentiment"] == "Neutral", neutral_reply_prompt | model | parser_str),
    RunnableLambda(lambda _: "Unable to select a reply for this sentiment."),
)

loaded_docs = loader.load()
review_text = loaded_docs[0].page_content
reviews = [part.strip() for part in review_text.split("\n\n") if part.strip()]
if not reviews:
    raise ValueError(f"No reviews found in {reviews_file}")

review_results = []
for number, review in enumerate(reviews, start=1):
    analysis = classification_chain.invoke({"review": review})
    reply = reply_chain.invoke(
        {
            "review": review,
            "summary": analysis.summary,
            "sentiment": analysis.sentiment,
        }
    )
    review_results.append(
        {
            "review_number": number,
            "review": review,
            "summary": analysis.summary,
            "sentiment": analysis.sentiment,
            "reply": reply,
        }
    )

print("Per-review analysis and replies:")
for result in review_results:
    print(
        f"\nReview {result['review_number']} [{result['sentiment']}]\n"
        f"Summary: {result['summary']}\nReply: {result['reply']}"
    )

reviews_for_analysis = "\n\n".join(reviews)
parallel_analysis_chain = RunnableParallel(
    {
        "summary": PromptTemplate(
            template=(
                "Summarize these customer reviews, noting the range of sentiment "
                "and any notable tradeoffs.\n\n{reviews}"
            ),
            input_variables=["reviews"],
        )
        | model
        | parser_str,
        "common_themes": PromptTemplate(
            template=(
                "Identify the most common customer praise and the most common "
                "complaint in these reviews. Use evidence from the text.\n\n{reviews}"
            ),
            input_variables=["reviews"],
        )
        | model
        | parser_str,
    }
)
final_report_prompt = PromptTemplate(
    template=(
        "Create a concise customer feedback report from these two analyses. "
        "Include an overall summary and the main praise and complaint.\n\n"
        "Summary analysis:\n{summary}\n\nCommon themes:\n{common_themes}"
    ),
    input_variables=["summary", "common_themes"],
)
parallel_results = parallel_analysis_chain.invoke({"reviews": reviews_for_analysis})
final_report_chain = final_report_prompt | model | parser_str
final_report = final_report_chain.invoke(parallel_results)

print("\nParallel analysis:")
print(f"Summary: {parallel_results['summary']}")
print(f"Common themes: {parallel_results['common_themes']}")
print("\nFinal report:")
print(final_report)

# Embed each review once, then rank them against a question using cosine similarity.
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
review_vectors = embeddings.embed_documents(reviews)
question = input("\nAsk a question to find the most relevant review: ").strip()
if question:
    question_vector = embeddings.embed_query(question)
    scores = cosine_similarity([question_vector], review_vectors)[0]
    best_index = int(scores.argmax())
    print(
        f"\nMost relevant review (similarity {scores[best_index]:.3f}):\n"
        f"{reviews[best_index]}"
    )

# Keep a message history so follow-up questions can refer to the report and reviews.
chat_history = [
    SystemMessage(
        content=(
            "You answer follow-up questions about the supplied customer reviews "
            "and report. Ground your answers in that context; say when it does not "
            "contain enough information."
        )
    ),
    HumanMessage(
        content=(
            f"Customer reviews:\n{reviews_for_analysis}\n\n"
            f"Analysis report:\n{final_report}"
        )
    ),
    AIMessage(content="I have reviewed the customer feedback. What would you like to know?"),
]

print("\nAsk follow-up questions about the report. Type 'exit' to finish.")
while True:
    question = input("You: ").strip()
    if question.lower() == "exit":
        break
    if not question:
        continue
    chat_history.append(HumanMessage(content=question))
    answer = model.invoke(chat_history)
    print(f"Assistant: {answer.content}")
    chat_history.append(AIMessage(content=answer.content))
