from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("9_splitter/gen_ai_interview.pdf")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=10000, chunk_overlap=0, separator='')    

result = text_splitter.split_documents(documents)
print(f"Number of documents: {len(result)}")
print(f"First document: {result[2].page_content}")