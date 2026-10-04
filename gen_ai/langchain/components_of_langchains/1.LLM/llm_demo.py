from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(
	model = 'gemini-2.5-flash'
)

res = llm.invoke("What is Capital Of Gujarat,India")

print(res)
