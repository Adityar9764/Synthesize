import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

openai.api_key = os.getenv("OPENAI_API_KEY")  # Set OpenAI API Key

def ask_question(question, context):
    prompt = f"Here is a document:\n\n{context}\n\nBased on this document, answer the following question:\n\n{question}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can use "gpt-3.5-turbo" if needed
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.5
    )
    
    return response["choices"][0]["message"]["content"]
