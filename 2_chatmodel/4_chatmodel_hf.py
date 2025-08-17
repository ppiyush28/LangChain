from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="openai/gpt-oss-20b", task ="text-generation",)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of France?")
print(response)
