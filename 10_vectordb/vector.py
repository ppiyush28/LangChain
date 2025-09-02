
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Create LangChain documents for IPL players
doc1 = Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"}
    )
doc2 = Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"team": "Mumbai Indians"}
    )
doc3 = Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings"}
    )
doc4 = Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"team": "Mumbai Indians"}
    )
doc5 = Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"team": "Chennai Super Kings"}
    )

docs = [doc1, doc2, doc3, doc4, doc5]

# Create a vector store using Chroma
vector_store = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory="chroma_db",
    collection_name="ipl_players"
)

# Add documents to the vector store
vector_store.add_documents(docs)

# Retrieve documents from the vector store
vector_store.get(include=["metadatas", "documents", "embeddings"], ids=["0", "1"])

#print vector store data
data = vector_store.get(include=["metadatas", "documents", "embeddings"])
print("Vector Store Data:")
for i in range(len(data["documents"])):
    print(f"Document {i+1}:")
    print(f"Content: {data['documents'][i]}")
    print(f"Metadata: {data['metadatas'][i]}")
    print(f"Embedding: {data['embeddings'][i]}")
    print()

#search for similar documents

query = "Who is the best captain in IPL?"
results = vector_store.similarity_search(query, k=2)  # Retrieve top 2 similar documents
for i, result in enumerate(results):
    print("similarity_search")
    print(f"Result {i+1}:")
    print(f"Content: {result.page_content}")
    print(f"Metadata: {result.metadata}")
    print()


#query = "Which bolwer is known for his yorkers?"
#query = "who among these are best bowler"
query = "Who is the best captain in IPL?"
results = vector_store.similarity_search_with_score(query, k=2)  # Retrieve top 2 similar documents
for i, (result, score) in enumerate(results):
    print("similarity_search_with_score")
    print(f"Result {i+1}:")
    print(f"Content: {result.page_content}")
    print(f"Metadata: {result.metadata}")
    print(f"Score: {score}")
    print()


# meta-data filtering
filter_data = vector_store.similarity_search_with_score(
    query="",
    filter={"team": "Chennai Super Kings"}
)

print("Vector Store Data:")
for i, (result, score) in enumerate(filter_data):
    print(f"Document {i+1}:")
    print(f"Content: {result.page_content}")
    print(f"Metadata: {result.metadata}")
    print(f"Score: {score}")
    print()


# update documents
updated_doc1 = Document(
    page_content="Virat Kohli1111, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
    metadata={"team": "Royal Challengers Bangalore"}
)

vector_store.update_document(document_id='09a39dc6-3ba6-4ea7-927e-fdda591da5e4', document=updated_doc1)

data = vector_store.get(include=["metadatas", "documents", "embeddings"], ids=['09a39dc6-3ba6-4ea7-927e-fdda591da5e4'])
print("Updated Document:")
for i in range(len(data["documents"])):
    print(f"Document {i+1}:")
    print(f"Content: {data['documents'][i]}")
    print(f"Metadata: {data['metadatas'][i]}")
    print(f"Embedding: {data['embeddings'][i]}")
    print()
