from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnablePassthrough 

model = ChatOllama(model='llama3')

prompt01 = PromptTemplate(
    template = "write a joke about {topic}",
    input_variable = ['topic']
)

parser = StrOutputParser()

prompt02 = PromptTemplate(
    template = "Explain the following joke : {joke}",
    input_variable = ['joke']
)

joke_gen_chain = RunnableSequence(prompt01 , model , parser)
parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough() ,#'joke' is a label ,what this output represents
    'explanaion' :RunnableSequence(prompt02 , model , parser)
})

chain = RunnableSequence(joke_gen_chain , parallel_chain)
print(chain.invoke({"topic":"Cricket"}))