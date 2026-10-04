import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from huggingface_hub import login

load_dotenv()
# print('Hf-token',HF_TOKEN)

# print(whoami(token=HF_TOKEN))

login()


llm = HuggingFaceEndpoint(
	repo_id='meta-llama/Llama-3.1-8B-Instruct',
	task='text-generation',
)

model = ChatHuggingFace(
	llm=llm
)

res = model.invoke('What is the capital of india')

print(res.content)


