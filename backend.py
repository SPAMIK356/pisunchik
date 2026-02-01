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


class UserParams(BaseModel):
    weight: float
    age : int
    sex : str
    goal : str


class Macros(BaseModel):
    kalories : float = Field(description="Кількість калорій")
    proteins : float = Field(description="Кількість білків")
    fats : float = Field(description="Кількість жирів")
    carbs : float = Field(description="Кількість вуглеводів")

class Meal(BaseModel):
    macros_and_cals : Macros = Field(description="Сумарна кількість поживних речовин та калорій на цей прийом їжі")
    dishes : list[str] = Field(description="Страви для цього прийому їжі")
    name : str = Field(description="Назва прийому їжі (наприклад, сніданок, вечеря, перекус і т.д.)")

class Plan(BaseModel):
    meals : list[Meal] = Field(description="Список прийомів їжі на цей день")
    macros_and_cals : Macros = Field(description="Сумарна калорійність та поживна цінність всіх вказаних прийомів їжі")
    note : str = Field(description="Додаткова інформація")

@app.post('/get_plan')
async def get_plan(userParams : UserParams):
    """"""