from google import genai
from dotenv import load_dotenv
from fastapi import FastAPI
from google.genai import errors

# Load the local key before creating the Gemini client.
load_dotenv()
MODEL_ID = "gemini-3.8-flash"
client = genai.Client()


async def generate(prompt: str)->str:
    try:
        response = await client.aio.models.generate_content(
            model = MODEL_ID,
            contents = prompt,
        )
    except errors.APIError as error:
        raise HTTPException(
            status_code=502, 
            detail="Gemini Request Failed",
        ) from error
    return response.text