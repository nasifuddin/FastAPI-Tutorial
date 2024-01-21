from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# creating a python dictionary which contains the information of the users
users = {
    46: {"name": "nasif", "age": 25, "email": "nasifuddinof@gmail.com"},
    37: {"name": "fabi", "age": 26, "email": "fabinahian1@gmail.com"},
}


# class for creating new user
class create_user(BaseModel):  # creating class for adding new user to the database
    name: str
    age: int
    email: str


# class for updating existing user
class update_user(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None


"""To update user we need to make make every attribute optional
so that the user has the control of the criteria's that they wanna
update.
"""


# creating an end point
"""There are four endpoint methods used in an API:
1. GET - GET AN INFORMATION 
2. POST - CREATE INFORMATION
3. PUT - UPDATE INFORMATION
4. DELETE - DELETE SOMETHING
"""


@app.get("/")  # this is a home getpoint
def index():
    return {"This is the homepage"}


# adding path parameters (search by id)
@app.get("/users/{id}")
def get_users(
    id: int = Path(description="Provide the ID of the user", gt=0, lt=100)
):  # user id must be greater than zero and less than hundred
    if id not in users:
        return {"error": "user not found"}
    return users[id]


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


# creating new user by post method
@app.post("/create-user/{id}")
def create_new_user(id: int, user: create_user):
    if id in users:
        return {"error": "user_id already exists"}

    users[id] = user
    return users[id]


# creating put method to update the existing information
@app.put("/update-user/{id}")
def update_user(id: int, update_user: update_user):
    if id not in users:
        return {"error": "user does not exist"}

    if update_user.name != None:
        users[id]["name"] = update_user.name

    if update_user.age != None:
        users[id]["age"] = update_user.age

    if update_user.email != None:
        users[id]["email"] = update_user.email

    return users[id]


# delete an user by using delete method
@app.delete("/delete-user/{id}")
def delete_user(id: int):
    if id not in users:
        return {"error": "user does not exist"}

    del users[id]
    return {"message": "user deleted"}
