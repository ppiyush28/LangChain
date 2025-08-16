from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
    model="gpt-4o",
    temperature=2,
    max_retries=0,
    request_timeout=10,
    streaming=True,
    verbose=True,
    max_tokens=6,
    seed=42,
    max_completion_tokens=10
 )    

response = model.invoke("What is the capital of france?")
print(response)  # Output: "The capital of France is Paris."
print(response.content)  # Output: "The capital of France is Paris."