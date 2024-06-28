import streamlit as st
from dotenv import load_dotenv

load_dotenv()
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a YouTube video summarizer. You will be taking transcript text and summarizing it into a short, concise summary."""


def generate_gemini_content(transcript_text, prompt):
    model = genai.load_model("gemini-pro")
    response = model.generate(prompt + transcript_text)
    return response.text
