from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda , RunnableSequence , RunnableParallel , RunnablePassthrough 

def word_count(text):
    return(len(text.split()))

prompt = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables = ['topic']
)

model = ChatOllama(model='llama3')
parser = StrOutputParser()

jokeGen_chain = RunnableSequence(prompt , model , parser )

parallel_chain = RunnableParallel({
    'joke' :RunnablePassthrough(),
    'word_count' : RunnableLambda(word_count)
})

final_chain = RunnableSequence(jokeGen_chain , parallel_chain)
result = final_chain.invoke({'topic':'AI'})
final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)