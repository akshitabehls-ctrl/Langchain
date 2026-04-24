from langchain_community.embeddings import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

emb = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)


document = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

doc_embed = emb.embed_documents(document)
# print(len(vectors))
# print(len(vectors[0]))
# print(vectors[:5])

query = "Tell me about Dhoni"
query_embed = emb.embed_query(query)

#Flatten
scores = cosine_similarity([query_embed],doc_embed)[0]
# index , score =sorted(list(enumerate(scores)),key = lambda x: x[1])[-1] #highest


#get best index
index = max(range(len(scores)),key = lambda x :scores[x]) #which index gives the highest score
score = scores[index]

print(query)
print(document[index])
print(f"similarity Score is {score}")