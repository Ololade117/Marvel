from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
load_dotenv()  
def get_gemini_response(message: str) -> str:
    """
    Takes a message and returns a response from Google Gemini AI.
    
    Args:
        message: The user's message to send to Gemini
        
    Returns:
        The AI-generated response as a string
    """
    genai.configure(api_key = (
        os.getenv("GEMINI_API_KEY")  # Codespaces / local env
        or st.secrets.get("GEMINI_API_KEY")  # Streamlit Cloud
    ))
    
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(message)
    
    return response.text