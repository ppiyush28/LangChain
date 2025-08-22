from pydantic import BaseModel, EmailStr, Field
from typing import Optional,Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


model = ChatOpenAI()

class Review(BaseModel):
    themes: list[str] = Field(..., description="The theme of the review")
    summary: str = Field(..., description="A brief summary of the review")
    sentiment: Literal['pos','neg'] = Field(..., description="The sentiment of the review (e.g., positive, negative, neutral)")
    rating: int = Field(..., ge=1, le=5, description="The rating given in the review (1 to 5 stars)")
    pros: Optional[list[str]] = Field(None, description="Pros mentioned in the review")
    cons: Optional[list[str]] = Field(None, description="Cons mentioned in the review")


strutuce_output = model.with_structured_output(Review)

result = strutuce_output.invoke(
    """
    This is langchain, a framework for developing applications powered by language models.
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
    """
)
print(result)
print(result.json())