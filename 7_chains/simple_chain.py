from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI()

prompt = PromptTemplate(
    template="What is the capital of {country}?",
    input_variables=["country"],
)

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({"country": "France"})

print(result)  # Output: Paris

chain.get_graph().print_ascii()  # Visualize the chain structure

