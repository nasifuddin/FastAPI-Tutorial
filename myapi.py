from fastapi import FastAPI

app = FastAPI()

# creating an end point
"""There are four endpoint methods used in an API:
1. GET - GET AN INFORMATION 
2. POST - CREATE INFORMATION
3. PUT - UPDATE
4. DELETE - DELETE SOMETHING
"""


@app.get("/")  # this is a home getpoint
def index():
    return {"name": "Nasif"}
