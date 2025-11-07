import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name:str

class Users(BaseModel):
    users: List[User]

app= FastAPI()

origins= [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"],
)

temp_db= {"Users":[]}

@app.get("/users", response_model= Users)
def get_users():
    return Users(users= temp_db["Users"])

@app.post("/users")
def add_user(user: User):
    temp_db["Users"].append(user)
    return {"message": "User added successfully"}
    return user 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)