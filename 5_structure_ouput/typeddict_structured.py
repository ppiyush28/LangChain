from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal


load_dotenv()

model = ChatOpenAI()


class Review(TypedDict):
    themes : Annotated[list[str], "List of themes or topics covered in the review"]
    rating : Annotated[int, "Rating given by the reviewer, typically on a scale of 1 to 5"]
    summary : Annotated[str, "A brief summary of the review"]
    #sentimnent: Annotated[str, "The sentiment of the review, e.g., positive, negative, neutral"]
    
    sentimnent : Annotated[Literal["positive1","negative2","neutral3","postive"],"Sentiment of the review, categorized as positive, negative, neutral, or postive"]
    pros: Annotated[Optional[list[str]], "List of positive aspects mentioned in the review"]
    cons: Annotated[Optional[list[str]], "List of negative aspects mentioned in the review"]

structured_output = model.with_structured_output(Review)

result = structured_output.invoke(""" This is langchain, a framework for developing applications powered by language models.
It is a collection of components that can be used to build applications that are more than just a simple chat interface. It is designed to be modular and flexible, allowing developers to create applications that can be customized to fit their needs.
Langchain is a framework for developing applications powered by language models.
structured output is a way to define the structure of the output that you want to receive from the model.
This is a simple example of how to use structured output in langchain.
procs :
1. It is a collection of components that can be used to build applications that are more than just a simple chat interface.
2. It is designed to be modular and flexible, allowing developers to create applications that can be customized to fit their needs.
3. Langchain is a framework for developing applications powered by language models.
cons:
1. It may require a learning curve for developers who are new to the framework.
2. The modular nature may lead to complexity in managing dependencies and components.
3. It may not be suitable for very simple applications where a straightforward chat interface suffices.
4. The performance may vary depending on the specific components and configurations used.
""")

         

print(result)
print('summary>>', result['summary'])
print('sentimnets>>', result['sentimnent'])



