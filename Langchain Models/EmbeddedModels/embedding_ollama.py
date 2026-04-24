from langchain_community.embeddings import HuggingFaceEmbeddings

emb = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

# # Example text
# text = "Cricket is a popular sport in India"

# # Get embedding
# vector = emb.embed_query(text)


docs = [
    "Cricket is popular in India",
    "Football is loved in Europe",
    "AI is transforming industries"
]

vectors = emb.embed_documents(docs)

print(len(vectors))   #no of sentences
print(len(vectors[0]))    # dim
print(vectors[:5])