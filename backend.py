from fastapi import FastAPI
from contextlib import asynccontextmanager
from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):

    load_dotenv()

    global client

    client = genai.Client()

    yield



app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)



@app.post('/get_plan')
async def get_plan():
    """"""