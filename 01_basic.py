import langchain
print(langchain.__version__)

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')
respone = llm.invoke("What is the capital of France?")
print(respone)

