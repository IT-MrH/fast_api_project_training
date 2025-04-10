from fastapi import FastAPI

from app.config import load_config
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


# Получение пользователя по параметру пути
@app.get('/users/{username}')
async def get_user(username: str):
    for user in fake_db:
        if user["username"] == username:
            return user
    return {"error": "User not found"}

# Получение списка пользователей с ограничением (параметр запроса)
@app.get("/users/")
async def read_users(limit: int = 10):
    return fake_db[:limit]

# Добавление нового пользователя (параметр тела запроса)
@app.post('/add_user', response_model=User)
async def add_user(user: User):
    fake_db.append({"username": user.username, "user_info": user.user_info})
    return user
@app.get('/')
async def home_page():
    return {"message": "HOME !"}