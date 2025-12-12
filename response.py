import google.generativeai as genai

def get_gemini_response(message: str) -> str:
    """
    Takes a message and returns a response from Google Gemini AI.
    
    Args:
        message: The user's message to send to Gemini
        
    Returns:
        The AI-generated response as a string
    """
    genai.configure(api_key="AIzaSyCAlkbyfWOuYsCzeNkjcTf_zYhaIjC9H5A")
    
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(message)
    
    return response.text