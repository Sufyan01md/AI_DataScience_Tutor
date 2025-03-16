
import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_google_genai import ChatGoogleGenerativeAI


import google.generativeai as genai
genai.configure(api_key="AIzaSyCuNiwxnuYsiKmlOVH30YnyI_RBiJUd-Qc") 


memory = ConversationBufferMemory(k=5)


model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3)


chain = ConversationChain(llm=model, memory=memory)


st.title("Conversational AI Data Science Tutor")
st.write("Ask any data science-related questions!")

user_input = st.text_input("Your Question:")
if st.button("Ask"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            response = chain.run(user_input)
        st.subheader("Tutor's Response:")
        st.write(response)
    else:
        st.warning("Please enter a question!")
