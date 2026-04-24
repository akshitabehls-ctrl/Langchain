from langchain_ollama import ChatOllama

# Initialize the Ollama chat model
llm = ChatOllama(model="llama3",temperature = 1.8)

# Example usage
response = llm.invoke("Write a 5 line poem on Cricket")
print(response.content)

#similar can be there for openai , antroptic , google gemini , huggling face APIs