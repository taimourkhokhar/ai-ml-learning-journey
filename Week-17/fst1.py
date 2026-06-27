from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "Taimour",
        "age": 23,
        "year": "Final Year"
    },
    2: {
        "name": "Zaim",
        "age": 21,
        "year": "First Year"
    }
}

class Student(BaseModel):
    name:str
    age:int
    year:str

class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    year:Optional[str]=None

@app.get("/")
def index():
    return {"name": "First Data"}

# Path Parameter
@app.get("/get-student/{student_id}")
def get_student(
    student_id: int = Path(
        ...,
        description="The ID of the student you want to show",
        gt=0
    )
):
    return students[student_id]



#query parameters 
@app.get("/get-by-name/{student_id}")
def get_students(student_id:int,name:str):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not found"}

#request body and post method


@app.post("/create-student/{student_id}")
def create_student(student_id:int,student:Student):
    if student_id in students:
        return {"Error":"Student exist"}
    students[student_id]=student
    return students[student_id]


#put method
@app.put("/update-student/{student_id}")
def update_student(student_id:int,student:UpdateStudent):
    if student_id not in students:
        return {"Error":"Students does not exist"}
    if student.name!=None:
        students[student_id].name=student.name
    if student.age!=None:
        students[student_id].age=student.age
    if student.year!=None:
        students[student_id].year=student.year
    return students[student_id]


#delete method

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error":"Student does not exist"}

    del students[student_id]
    return {"Message":"Student deleted successfully"}    