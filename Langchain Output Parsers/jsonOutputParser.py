from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

model = ChatOllama(model = 'llama3') #dies not give structured output by default

parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables = {"format_instruction": parser.get_format_instructions()}
)
chain = template | model | parser 
result = chain.invoke({'topic':'black_hole'})
print(result)  