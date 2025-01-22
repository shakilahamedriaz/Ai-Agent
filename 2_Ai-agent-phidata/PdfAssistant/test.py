import os
from dotenv import find_dotenv, load_dotenv

# Load .env file
load_dotenv()

# Debug environment variable loading
print(f"Loading .env file from: {find_dotenv()}")
print(f"GROQ_API_KEY value: {os.getenv('GROQ_API_KEY')}")
print(f"GROQ_API_KEY: {os.getenv('GROQ_API_KEY')}")