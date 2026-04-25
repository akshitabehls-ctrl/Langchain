from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

model = ChatOllama(model='llama3')

prompt01 = PromptTemplate(
    template = "write a joke about {topic}",
    input_variable = ['topic']
)

parser = StrOutputParser()

prompt02 = PromptTemplate(
    template = "Explain the following joke :\n {joke}",
    input_variable = ['joke']
)

chain = RunnableSequence(prompt01 , model , parser , prompt02 , model , parser)

print(chain.invoke({'topic': 'Modi'}))