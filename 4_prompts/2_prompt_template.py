from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

model = ChatOpenAI(
    model="gpt-4-turbo",
    temperature=2,
    max_retries=0,
    request_timeout=10,
    streaming=True,
    verbose=True,
    max_tokens=6,
    seed=42,
    max_completion_tokens=10
)

template1 = PromptTemplate(
    input_variables=["question"],
    template="""You are a helpful assistant.""")
    
prompt = template1.invoke(
    {
        "question": "What is the capital of France?"
    },
)

response = model.invoke(prompt)
print(response)  # Output: "The capital of France is Paris."