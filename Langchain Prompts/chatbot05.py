from langchain_ollama import ChatOllama 
from langchain_core.messages import HumanMessage , SystemMessage , AIMessage
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder

model = ChatOllama(model='llama3')

#chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer Support agent'),
    MessagesPlaceholder(variable_name='chat_history'), #injects past messages into the prompt dynamically 
    ('human','{query}')
])

chat_history = []

with open('chat_history.txt') as f :
    chat_history.extend(f.readlines()) 
    #append- put box inside box 
    #extend - open the box and pour the items inside

prompt = chat_template.invoke({
    'chat_history' : chat_history,
    'query': HumanMessage(content = 'Where is my refund')
})

result = model.invoke(prompt)
print(result)
print(prompt)