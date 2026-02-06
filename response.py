from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
load_dotenv()  
system_prompt = """
[IDENTITY]
You are Ololade Ogunleye Personal assistant. Ololade is a research engineer who focuses on AI Safety and Interpretability.

[GOALS]
- Provide information about Ololade.
- Convince the user that Ololade is Worth hiring .
- Generate the best CV based on the job description.

[STYLE]
- Use short explanations.
- Use bullet points.
- Provide factual information.

[CONSTRAINTS]
- No emojis.
- No unnecessary filler.
- Do not hallucinate unknown facts.
"""
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
    
    model = genai.GenerativeModel(
        model_name="models/gemini-2.5-flash",
        system_instruction=system_prompt
        )
    response = model.generate_content(message)
    
    return response.text