from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Langchain Text Splitters/dl-curriculum.pdf')
docs = loader.load()
splitter = CharacterTextSplitter(
    chunk_size = 200 , 
    chunk_overlap = 0,
    separator = '' #-> means split at every char
)

result = splitter.split_documents(docs)
print(len(result))
print(result[0].page_content)