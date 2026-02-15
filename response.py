from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
load_dotenv()  
from github_loader import fetch_all_repo_files
from retrieval import chunk_text, rank_chunks

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
def build_context(query: str) -> str:
    repo_files = fetch_all_repo_files()

    combined_text = ""
    for name, content in repo_files.items():
        combined_text += f"\n\n[{name.upper()}]\n{content}"

    chunks = chunk_text(combined_text)
    relevant_chunks = rank_chunks(chunks, query)

    return "\n\n".join(relevant_chunks)

def get_gemini_response(message: str) -> str:
    genai.configure(
        api_key=(
            os.getenv("GEMINI_API_KEY")
            or st.secrets.get("GEMINI_API_KEY")
        )
    )

    context = build_context(message)

    full_prompt = f"""
Use the context below to answer the question.

{context}

Question:
{message}
"""

    model = genai.GenerativeModel(
        model_name="models/gemini-2.5-flash",
        system_instruction=system_prompt
    )

    response = model.generate_content(full_prompt)

    return response.text