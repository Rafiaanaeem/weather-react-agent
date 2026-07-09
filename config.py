import os
from dotenv import load_dotenv

# Load environment variables from the .env file into os.environ
load_dotenv()

# Fetch the API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# If these keys are missing, the agent cannot function. We raise an error immediately.
if not GROQ_API_KEY:
    raise ValueError("CRITICAL ERROR: GROQ_API_KEY is missing. Please set it in the .env file.")

if not TAVILY_API_KEY:
    raise ValueError("CRITICAL ERROR: TAVILY_API_KEY is missing. Please set it in the .env file.")
