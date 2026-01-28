from fastapi import FastAPI
from dotenv import load_dotenv
from app.mpesa.auth import get_access_token
import os

load_dotenv()

app = FastAPI(title="M-Pesa Tracker API")

@app.get("/")
def read_root():
    return {"message": "M-Pesa Tracker API is running!"}

@app.get("/mpesa-auth-test")
def test_auth():
    """Test if we can get M-Pesa access token"""
    consumer_key = os.getenv("MPESA_CONSUMER_KEY")
    return {
        "status": "success" if consumer_key else "error",
        "message": "Credentials loaded" if consumer_key else "No credentials found",
        "consumer_key_first_4": consumer_key[:4] + "..." if consumer_key else None
    }

@app.get("/test-mpesa-auth")
def test_mpesa_auth():
    """Test M-Pesa authentication"""
    result = get_access_token()
    return result