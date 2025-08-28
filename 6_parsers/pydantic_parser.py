from dotenv import load_dotenv
from langchain_huggingface import HuggingFacePipeline, HuggingFaceEndpoint, ChatHuggingFace

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    tastk="text-generation",
)

model = ChatHuggingFace(llm=llm)


class User(BaseModel):
    name: str = "John Doe"
    age: int = 30
    city : str = "New York"

parser = PydanticOutputParser(pydantic_object=User)

template1 = PromptTemplate(
    template="genrated name, age, citi of fictional {place} person \n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# chain = template1 | model | parser

# final_result = chain.invoke({"place": "Indian"})
# print("Parsed result:>>>", final_result)


prompt = template1.invoke({"place":"Indian"})
result = model.invoke(prompt)

print("result:>>>", result)

final_result = parser.parse(result.content)
print("Parsed result:>>>", final_result)
