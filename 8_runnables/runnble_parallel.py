from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()
llm = ChatOpenAI()

prompt1 = PromptTemplate(
    template="genrate a tweet about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="genrate a linkedin post about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

parallel_runnable = RunnableParallel({
    "tweet": RunnableSequence(prompt1, llm, parser),
    "linkedin_post": RunnableSequence(prompt2, llm, parser)
})

chain = parallel_runnable.invoke({"topic": "funny"})
print(chain)