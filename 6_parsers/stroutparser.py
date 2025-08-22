from dotenv import load_dotenv
from langchain_huggingface import HuggingFacePipeline, HuggingFaceEndpoint, ChatHuggingFace

from langchain_core.prompts import PromptTemplate


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    tastk="text-generation",
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="You are a helpful assistant. Answer the question: {question}",
    input_variables=["question"]
)

template2 = PromptTemplate(
    template="You are a summarization. Summarize the following text: {data}",
    input_variables=["data"]
)

prompt1 = template1.invoke({"question": "What is the capital of France?"})
response1 = model.invoke(prompt1)

print("Response to question:", response1)

prompt2 = template2.invoke({"data": "Paris is the capital of France. It is known for its art, fashion, and culture."})
response2 = model.invoke(prompt2)
print("Response to summarization:", response2)

