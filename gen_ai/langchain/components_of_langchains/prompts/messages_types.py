from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')


messages = [
	SystemMessage(content='You are the ai assistant with purpose of dealing with the user in a polite manner'),
	HumanMessage(content='Tell me about top 5 places names in India just names')	
]

res = model.invoke(messages)

messages.append(AIMessage(res.content))

print(messages)



