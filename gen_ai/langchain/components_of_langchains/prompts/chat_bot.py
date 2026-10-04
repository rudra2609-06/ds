from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()


model = ChatGoogleGenerativeAI(
	model='gemini-2.5-flash'
)

chat_history = [
	SystemMessage('You are a cost effecient ai assistant serving the purpose of chat bot replying to user queries with minimal tokens')
]

while True:
	user_input = input('You: ')
	if user_input == 'exit':
		break
	chat_history.append(HumanMessage(user_input))
	result = model.invoke(chat_history)
	print('AI: ',result.content)
	chat_history.append(AIMessage(result.content))

print(chat_history)


