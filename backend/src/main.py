import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

# Create an OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Test GPT connection
try:
    response = client.chat.completions.create(
        model="gpt-4o",  # Use your preferred model ID here
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! Can you confirm you're working?"}
        ]
    )
    print("OpenAI Response:", response.choices[0].message.content)
except Exception as e:
    print("Failed to connect to OpenAI:", e)