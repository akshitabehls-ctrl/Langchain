import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# Load local model
model = ChatOllama(model="llama3", temperature=0.7)

st.header('📄 Research Paper Explainer')

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Prompt template (instead of JSON)
template = PromptTemplate(
    input_variables=["paper", "style", "length"],
    template="""
Explain the research paper "{paper}".

Explanation style: {style}
Explanation length: {length}

Make the explanation clear and structured.
"""
)

if st.button('Summarize'):
    st.write("Running...")
    chain = template | model

    result = chain.invoke({
        "paper": paper_input,
        "style": style_input,
        "length": length_input
    })

    st.write(result.content)