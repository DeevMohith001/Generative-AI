from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Loads the GOOGLE_API_KEY from .env into os.environ
load_dotenv()

# Initialize the model
llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

# Invoke the model
response = llm.invoke("What is the capital of India")
print(response)