from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()



llm = ChatAnthropic(
    model="claude-2")

response = llm.invoke("What is the capital of France?")
print(response)