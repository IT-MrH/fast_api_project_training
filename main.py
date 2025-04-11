from fastapi import FastAPI

from app.config import load_config
from app.models.feedback import Feedback
from app.models.user import User


app = FastAPI()
config = load_config()

if config.debug:
    app.debug = True
else:
    app.debug = False

fake_db = [
    {"username": "vasya", "user_info": "любит колбасу"},
    {"username": "katya", "user_info": "любит петь"}
]
feedback_list = []


@app.get('/users/{username}')
async def get_user(username: str):
    for user in fake_db:
        if user["username"] == username:
            return user
    return {"error": "User not found"}


@app.get("/users/")
async def read_users(limit: int = 10):
    return fake_db[:limit]


@app.post("/feedback")
async def feedback_users(fbk: Feedback, is_premium: bool = None):
    feedback_list.append(fbk.dict())
    if is_premium:
        return {
            "message": f"Спасибо, {fbk.name}! Ваш отзыв сохранён. Ваш отзыв будет рассмотрен в приоритетном порядке."}
    return {"message": f"Спасибо, {fbk.name}! Ваш отзыв сохранён."}


@app.post('/add_user', response_model=User)
async def add_user(user: User):
    fake_db.append({"username": user.username, "user_info": user.user_info})
    return user


@app.get('/')
async def home_page():
    return {"message": "HOME !"}
