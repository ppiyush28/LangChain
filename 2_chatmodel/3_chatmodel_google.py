from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    max_tokens=10,
    #seed=1,
    top_p=0.9,
    top_k=40,

)

response = llm.invoke("What is the capital of France?")
print(response)
print(response.content)