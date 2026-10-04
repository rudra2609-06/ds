from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(
							   model='gemini-2.5-flash',
                               temperature=0.2,
                               max_completion_tokens = 10
							   )

res = model.invoke("Write 5 lines about pm narendra modi")

# print(res)
print(res.content)
