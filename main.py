from fastapi import FastAPI
from config import load_config
from logger import logger
from models.user import User

config = load_config()
app = FastAPI()

if config.debug:
    app.debug = True
else:
    app.debug = False


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/custom")
def read_custom_message(num1: int) -> dict:
    return {"message": num1}


@app.get("/db")
def get_db_info():
    logger.info(f"Connecting to database: {config.db.database_url}")
    return {"database_url": config.db.database_url}


user_info_test = User(name="John Doe", id=1)


@app.get("/user")
def get_user_info():
    print("zaxodet")
    return {"message": "Hello, World!"}