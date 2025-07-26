from llama_index.llms.azure_openai import AzureOpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")

llm = AzureOpenAI(engine="gpt-4.1", model="gpt-4.1", temperature=0.0)


def pdf():
    # print("Ingesting PDF...")
    response = llm.complete("The sky is a beautiful blue and")
    print(response)
