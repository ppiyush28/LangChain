from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableLambda, RunnableBranch
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

chatopenai = ChatOpenAI()


google_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    max_tokens=10,
    #seed=1,
    top_p=0.9,
    top_k=40,

)

parser = StrOutputParser()

class Sentiment(BaseModel):
    sentiment: Literal['positive', 'negative', 'neutral'] = Field(
        ..., description="The sentiment of the feedback"
    )

parser2 = PydanticOutputParser(pydantic_object=Sentiment)

prompt1 = PromptTemplate(
    template='classify the sentiment of following text as positive, negative or neutral: {feedback} \n {format_instuction}',
    input_variables=['feedback'],
    partial_variables={'format_instuction': parser2.get_format_instructions()},


)

classifier_chain = prompt1 | chatopenai | parser2

prompt2 = PromptTemplate(
    template="write appropriate response to this positive feedback: {feedback} \n",
    input_variables=['feedback']
)


respone = classifier_chain.invoke({'feedback': 'I love programming!'}).sentiment
print(respone)

prompt3 = PromptTemplate(
    template="write an appropriate respone to this negative feedback: {feedback} \n",
    input_variables=['feedback']
)

brached_chain = RunnableBranch(
    ( lambda x: x.sentiment == 'positive' ,  prompt2 | chatopenai | parser),
    ( lambda x: x.sentiment == 'negative',   prompt3 | google_model | parser),
    RunnableLambda(lambda x : "could not classify the sentiment")
)

final_chain = classifier_chain | brached_chain

response = final_chain.invoke(respone, {'feedback': 'I dnt love programming!'})
print(response)

final_chain.get_graph().print_ascii()