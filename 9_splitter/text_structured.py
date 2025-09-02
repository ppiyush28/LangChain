from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


documents = PyPDFLoader("9_splitter/gen_ai_interview.pdf").load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separators=["\n\n", "\n", " ", ""]
)
result = text_splitter.split_documents(documents)
print(f"Number of documents: {len(result)}")
print(f"First document: {result[4].page_content}")