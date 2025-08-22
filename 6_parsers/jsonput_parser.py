from dotenv import load_dotenv
from langchain_huggingface import HuggingFacePipeline, HuggingFaceEndpoint, ChatHuggingFace

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    tastk="text-generation",
)

model = ChatHuggingFace(llm=llm)

parser= JsonOutputParser()

template1 = PromptTemplate(
    template="You are a helpful assistant. Answer the question: {format_instruction}",
    input_variables=[],
    partial_variables= { 'format_instruction' : parser.get_format_instructions() }
)

prompt = template1.format()

print(prompt)

# chain = template1 | model | parser

# response = chain.invoke({"question": "What is the capital of France?"})
# print("Response to question:", response)

result = model.invoke(prompt)
print("Response to question:", result)

final_result = parser.parse(result.content)
print("Parsed result:>>>", final_result)