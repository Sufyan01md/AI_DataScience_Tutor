import streamlit as st
import google.generativeai as genai
from langchain.memory import ConversationBufferMemory

# Configure Google Gemini API
genai.configure(api_key="AIzaSyB92k02wczwkOK3VWuLQZ5JyJWj-uAV6Tk")

# Initialize memory
if 'memory' not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

def ask_tutor(query):
    """Send the user's data science-related query to Google Gemini AI with conversation memory."""
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    
    conversation_history = st.session_state.memory.load_memory_variables({})['history']
    prompt = f"""
    You are an AI Data Science Tutor. Your task is to help the user with their data science queries.
    Only answer questions related to data science, including statistics, machine learning, deep learning, and data analysis.
    If a question is not related to data science, politely refuse to answer.
    Maintain context from previous exchanges to provide coherent and context-aware responses.
    
    Conversation History:
    {conversation_history}
    
    User's Question:
    {query}
    """
    response = model.generate_content(prompt)
    reply_text = response.text if hasattr(response, "text") else str(response)
    
    # Update memory
    st.session_state.memory.save_context({'query': query}, {'response': reply_text})
    
    return reply_text

st.title("Conversational AI Data Science Tutor")
st.write("Ask your data science doubts and get AI-powered explanations with memory-enabled conversation.")

query_input = st.text_area("Enter your data science question:", height=200)

if st.button("Ask Tutor"):
    if query_input.strip():
        with st.spinner("Thinking..."):
            tutor_response = ask_tutor(query_input)
        
        st.subheader("Tutor's Response")
        st.write(tutor_response)
    else:
        st.warning("Please enter a data science-related question!")

# Option to clear conversation memory
if st.button("Clear Conversation Memory"):
    st.session_state.memory.clear()
    st.success("Memory cleared!")
