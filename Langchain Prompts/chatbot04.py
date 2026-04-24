from langchain_ollama import ChatOllama 
from langchain_core.messages import HumanMessage , SystemMessage , AIMessage
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(model='llama3')

# chat_template = ChatPromptTemplate([
#     SystemMessage(content = 'You are a helpful {domain} expert'),
#     HumanMessage(content= 'Explain in simple terms  what is {topic}') 
#     #these work better for static 
# ])

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human','Explain in simple terms , what is {topic}')
])

prompt = chat_template.invoke({
    'domain': 'cricket',
    'topic' : 'a Six'
})

result = model.invoke(prompt)
print(result.content)
# template.invoke -> Fills the placeholders in the template with 
# actual values and returns the final prompt