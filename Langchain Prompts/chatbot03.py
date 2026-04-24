from langchain_ollama import ChatOllama 
from langchain_core.messages import HumanMessage , AIMessage , SystemMessage
model = ChatOllama(model = 'llama3')

chat_history = [
    SystemMessage(content='You are a helpfull assistant and cracks jokes here and there')
    #Instructions for how model should behave 
]
while True :
    user_input = input("You:")
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content =result.content))
    print(f"AI:{result.content}")

print(chat_history)
