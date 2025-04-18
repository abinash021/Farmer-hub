import streamlit as st
from langchain_groq import ChatGroq
# Set up your ChatGroq instance
llm = ChatGroq(
    temperature=0,
    groq_api_key='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',  # replace this with your real key or store it safely using Streamlit secrets
    model_name="meta-llama/llama-4-scout-17b-16e-instruct"
)

# Streamlit UI
st.set_page_config(page_title="FarmAI - Crop and Disease Help", layout="centered")
st.title("🌾 FarmAI Assistant")
st.write("Ask about crop care, disease treatment, pest control, and more!")

# Input from the user
query = st.text_input("Type your farming-related question here:")

if st.button("Get Advice"):
    if query:
        with st.spinner("Thinking..."):
            try:
                response = llm.invoke(query)
                st.success("Here’s what I found:")
                st.write(response.content)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter a question to get started.")
