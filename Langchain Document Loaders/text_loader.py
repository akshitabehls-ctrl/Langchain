from langchain_ollama import ChatOllama
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model= 'llama3')

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader("Langchain Document Loaders/cricket.txt",encoding='utf-8') 
""" txt files are raw bytes , encoding tells python how to interpret those bytes as char """

docs = loader.load()

print(docs)
print(type(docs))
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))
