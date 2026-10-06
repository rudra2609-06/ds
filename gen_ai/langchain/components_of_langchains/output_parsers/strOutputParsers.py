from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from huggingface_hub import login
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


login()

llm = HuggingFaceEndpoint(
	repo_id='meta-llama/Llama-3.1-8B-Instruct',
	task= 'text-generation'
)

model = ChatHuggingFace(
	llm = llm	
)


t1 = PromptTemplate(
	template="Write a detailed report on topic {topic}",
	input_variables=['topic']
)

t2 = PromptTemplate(
	template="Write a 5 line summary on following text on report \n {text}",
	input_variables=['text']
)

# p1 = t1.invoke({'topic' : 'black-hole'})


# res1 = model.invoke(p1)

# p2 = t2.invoke({'text' : res1.content})

# res2 = model.invoke(p2)

# print(res2.content)



# ---------------------- With help of strOutputParsers ----------------------

# we would have to make a seperate chains if we would have used res.content
# we have used StrOutputParser thereby we can do it easily


parser = StrOutputParser()

chain = t1 | model | parser | t2 | model | parser

res1 = chain.invoke({'topic' : 'black-hole'})

print(res1)




