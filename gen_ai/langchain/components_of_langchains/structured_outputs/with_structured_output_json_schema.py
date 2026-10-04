from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, List

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')


# schema

schema = {
  "properties": {
    "summary": {
      "description": "A breif summary for the provided review",
      "title": "Summary",
      "type": "string"
    },
    "sentiment": {
      "description": "Return sentiment Positive, Negatie or Neutral",
      "title": "Sentiment",
      "type": "string"
    }
  },
  "required": ["summary", "sentiment"],
  "title": "Review",
  "type": "object"
}

structured_model = model.with_structured_output(schema)


# instead of invoking a model we will invoke now structured_model
res = structured_model.invoke("""
Hardware is good but when i operate it using windows i was unable to operate it thereby i tried to look into lot of yt vedios and then i fixed it manually unlike it should already be by any technical person from your side
""")

print(res)
