from fastapi import FastAPI
from pydantic import BaseModel



app=FastAPI()

@app.get("/")
def home():
  return {"Hello":"Taimour"}


#get method
@app.get("/student")
def student():
  return{
    "name":"Taimour",
    "age":23
  }
  
#post method
@app.post("/login")
def login():
  return{
    "status":"Logged In"
  }
  
#path parameter
@app.get("/student/{id}")
def student_id(id:int):
  return {"student":id}
  
  
@app.get("/search")
def search(name:str):
  return {"name":name}


class Student(BaseModel):
  name:str
  age:int
  
@app.post("/add")
def add_student(student:Student):
  return student