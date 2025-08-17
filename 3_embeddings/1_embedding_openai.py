from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=2)

response = embedding.embed_query("What is the capital of France?")
print(response)