from fastapi import FastAPI

app = FastAPI()

# creating a python dictionary which contains the information of the users
users = {
    47: {"name": "nasif", "age": 25, "email": "nasifuddinof@gmail.com"},
    36: {"name": "fabi", "age": 26, "email": "fabinahian1@gmail.com"},
}

# creating an end point
"""There are four endpoint methods used in an API:
1. GET - GET AN INFORMATION 
2. POST - CREATE INFORMATION
3. PUT - UPDATE
4. DELETE - DELETE SOMETHING
"""


@app.get("/")  # this is a home getpoint
def index():
    return {"This is the homepage"}


@app.get("/users/{user_id}")  # adding path parameters
def get_users(user_id: int):
    return users[user_id]
