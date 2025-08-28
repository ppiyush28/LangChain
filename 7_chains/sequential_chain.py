from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI()

prompt1 = PromptTemplate(
    template="genrate a details report on {topic}",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="genrate a 5 pointer summary from the following report: {report}",
    input_variables=["report"]
)
parser = StrOutputParser()

chain = prompt1 | llm | parser | prompt2 | llm | parser

response = chain.invoke({"topic": "AI in healthcare"})
print(response)

chain.get_graph().print_ascii()  # Visualize the chain structure
