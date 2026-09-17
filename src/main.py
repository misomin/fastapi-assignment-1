import fastapi
from src.dto import CreateUserRequest, UserResponse
from fastapi import Query

app = fastapi.FastAPI()

user_db = {}


@app.post("/api/users")
def create_user(request: CreateUserRequest) -> UserResponse:
    user_id = len(user_db) + 1
    user_db[user_id] = request.model_dump()

    return UserResponse(
        user_id=user_id,
        **user_db[user_id],
    )



@app.get("/api/users/{user_id}")
def get_user(user_id: int) -> UserResponse:
    if user_id not in user_db:
        raise ValueError(f"user_id {user_id}에 해당하는 사용자가 없습니다.")

    return UserResponse(
        user_id=user_id,
        **user_db[user_id],
    )
    # Todo
    



@app.get("/api/users")
def get_users(
    min_height: float = Query(...),
    max_height: float = Query(...),

) -> list[UserResponse]:
    # Todo

    return [
        UserResponse(user_id=user_id, **user)
        for user_id, user in user_db.items()
        if min_height <= user["height"] <= max_height
    ]