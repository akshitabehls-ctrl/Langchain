from langchain_ollama import ChatOllama 
model = ChatOllama(model = 'llama3')

chat_history = []
while True :
    user_input = input("You:")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print(f"AI:{result.content}")

print(chat_history)
#Since the chathistory is available with the model  
#it is able to get the context
'''
Problem : THe model does not have the context of which message is 
sent by whom since they are all list of strings
Solution : Maintain a dict 
'''