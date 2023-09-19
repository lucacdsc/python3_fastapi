from fastapi import FastAPI

from fast_zero.schemas import UserDb, UserPublic, UserSchema

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


database = []


@app.post('/users/', status_code=201, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDb(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id
