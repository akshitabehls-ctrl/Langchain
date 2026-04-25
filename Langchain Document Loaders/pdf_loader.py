from langchain_ollama import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model= 'llama3')

loader =PyPDFLoader("Langchain Document Loaders/dl-curriculum.pdf")
docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)