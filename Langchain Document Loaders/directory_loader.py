from langchain_ollama import ChatOllama
from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model= 'llama3')

loader = DiretoryLoader{
    path ='books',
    glob = '*.pdf' ,
    loader_cls = PyPDFLoader
}

docs = loader.load()

for document in docs:
    print(document.metadata)