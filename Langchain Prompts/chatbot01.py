from langchain_ollama import ChatOllama 
model = ChatOllama(model = 'llama3')
while True :
    user_input = input("You:")
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    print(f"AI:{result.content}")
 """#But here the model / calls are stateless
 (.venv) PS D:\AI\Projects\Langchain\Langchain Prompts> python -u "d:\AI\Projects\Langchain\Langchain Prompts\chatbot.py"
You:What is the capital of India
AI:The capital of India is New Delhi.
You:which is smaller 2.3 or 2.0
AI:That's an easy one!

2.0 is smaller than 2.3.
You:please multiply the smaller number with 10
AI:I'd be happy to help! However, I don't see a smaller number provided. Could you please share the numbers you'd like me to work with? I'll be happy to multiply the smaller one by 10 for you!
You:
  """

