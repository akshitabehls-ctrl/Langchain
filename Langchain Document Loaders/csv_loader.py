from langchain_ollama import ChatOllama
from langchain_community.document_loaders import CSVLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model= 'llama3')

loader = CSVLoader(file_path = "Langchain Document Loader/Social_Network_Ads.csv")
docs = loader.load()
print(len(docs))
print(docs[1])