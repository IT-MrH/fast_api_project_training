from fastapi import FastAPI

from app.config import load_config
from app.models.user import User

app = FastAPI()

config = load_config()

if config.debug:
    app.debug = True
else:
    app.debug = False


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


@app.post("/user")
def user_is_adult(usr: User):
    return usr.json()
