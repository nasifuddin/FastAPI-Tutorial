from fastapi import FastAPI, Path
from typing import Optional

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


# adding path parameters
@app.get("/users/{user_id}")
def get_users(
    user_id: int = Path(description="Provide the ID of the user", gt=0, lt=100)
):  # user id must be greater than zero and less than hundred
    return users[user_id]


# adding query parameters
@app.get("/users-name/{id}")
def get_users_by_name(
    *,
    id: int,
    name: Optional[str] = None,
):  # combining query parameter and path parameter
    for user_id in users:
        if users[user_id]["name"] == name:
            return users[user_id]

        elif user_id == id:
            return users[user_id]
    return {"user": "Not found"}


"""Python doesn't allow optional arguement before required aguement.
   Example:
   
        def get_users_by_name(
    name: Optional[str] = None, test: int)
    
    This will give an error. To solve this, you can do the following:
    
        def get_users_by_name(*,
    name: Optional[str] = None, test: int)

"""
