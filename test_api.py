import os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key is None: 
  print("Error: OpenAI API Key not found.")
else:
  print("OpenAI API key loaded successfully")
