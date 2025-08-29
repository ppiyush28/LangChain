from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()
llm = ChatOpenAI()

prompt = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

runnable = RunnableSequence(prompt, llm, parser)

chain = runnable.invoke({"topic": "funny"})
print(chain)  