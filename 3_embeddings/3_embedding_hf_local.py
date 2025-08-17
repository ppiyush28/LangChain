from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},  # Change to "cuda" if you have a GPU
)
#
text = "Paris is the capital of France"
embedding = embeddings.embed_query(text)
print(f"Embedding for '{text}': {embedding}")

documents = ["Paris is the capital of France.",
    "Berlin is the capital of Germany.",
    "Madrid is the capital of Spain."]
embeddings_list = embeddings.embed_documents(documents)
print(f"Embeddings for {texts}: {embeddings_list}")
