from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
import json
from dotenv import load_dotenv

load_dotenv()

class Review(BaseModel):
	summary : str = Field(...,description='A breif summary for the provided review')
	sentiment : str = Field(...,description='Return sentiment Positive, Negatie or Neutral')

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

structured_model = model.with_structured_output(Review)

# res = structured_model.invoke("""
# Hardware is good but when i operate it using windows i was unable to operate it thereby i tried to look into lot of yt vedios and then i fixed it manually unlike it should already be by any technical person from your side
# """)

# print(res)


# this is how you can generate your json schema from pydantic model
# print(json.dumps(Review.model_json_schema(),indent=2))