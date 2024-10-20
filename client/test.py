import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL", "http://0.0.0.0:8000")
print(BACKEND_URL)
