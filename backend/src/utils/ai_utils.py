import os  # Import os to access environment variables.
from openai import OpenAI  # Import OpenAI to communicate with the API.
from dotenv import load_dotenv  # Load environment variables from .env.

# Load environment variables
load_dotenv()  # This ensures that the API key is loaded.

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Create an OpenAI client using the API key.

def generate_response(prompt):
    """
    Sends a prompt to OpenAI and returns the response.
    :param prompt: The input string for GPT.
    :return: The generated response string.
    """
    try:
        # Make a call to the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4",  # Specify the GPT model to use.
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract and return the assistant's message
        return response.choices[0].message.content
    except Exception as e:
        # Return the error message if something goes wrong
        return f"Error generating response: {str(e)}"