from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence , RunnableParallel 
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model='llama3')

prompt1 = PromptTemplate(
    template = 'Generate a tweet about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a Linkedin post about {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1 , model , parser) ,
    'linkedin' : RunnableSequence(prompt2 , model , parser)
})

result = parallel_chain.invoke({'topic':'Education System'})
print(result)
print('-' * 50)
print(result['tweet'])
print('-' * 50)
print(result['linkedin'])