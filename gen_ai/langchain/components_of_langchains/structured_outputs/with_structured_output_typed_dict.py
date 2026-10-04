from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')


# schema
class Review(TypedDict):
	summary : Annotated[str,"A breif review summary"]
	sentiment: Annotated[str,"Return sentiment of review from positive,negative or neutral"]

structured_model = model.with_structured_output(Review)


# instead of invoking a model we will invoke now structured_model
res = structured_model.invoke("""
Hardware is good but when i operate it using windows i was unable to operate it thereby i tried to look into lot of yt vedios and then i fixed it manually unlike it should already be by any technical person from your side
""")

print(res)
