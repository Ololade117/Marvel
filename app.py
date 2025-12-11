import streamlit as st

st.set_page_config(page_title="Marvel Chatbot", page_icon="🦸", layout="wide")

st.title("🦸 Marvel Chatbot")
st.write("Chat with your friendly Marvel assistantBFF!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything about Marvel..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        response = f"Marvel assistant: I'm here to help! You asked: '{prompt}'. How can I assist you further?"
        st.markdown(response)
    
    # Add assistant message to history
    st.session_state.messages.append({"role": "assistant", "content": response})