import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key is None: 
  print("Error: OpenAI API Key not found.")
else:
  client = OpenAI()
  response = client.responses.create(
    model="gpt-5",
    input="Reply with exactly: API connection successful."
  )

  print(response.output_text)
