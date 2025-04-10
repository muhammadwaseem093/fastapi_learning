from fastapi import FastAPI 
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str

@app.get('/')
def root():
    return {"message": "Hello world"}

@app.post("/createposts")
def create_posts(new_post:Post):
    print(new_post)
    return {"data": "new post"}