from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class ProfileInfo(BaseModel):
    short_description: str
    long_bio: str

class User(BaseModel):
    username: str
    profile_info: ProfileInfo
    liked_posts: Optional[list[int]] = None


def get_user_info() ->User:
    profile_info = {
        "short_description": "My bio description",
        "long_bio": "This is longer bio"
    }

    profile_info = ProfileInfo(**profile_info)
    user_content = {
        "username": 1,
        "liked_posts":["this is gonna be a great post"],
        "profile_info": profile_info
    }
    return User[**user_content]

@app.get("/user/")
