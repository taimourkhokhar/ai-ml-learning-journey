from fastapi import FastAPI,Path



app=FastAPI()


students={
  1: {
    "name":"taimour",
    "age":17,
    "class":"Year 12"
  }
}


@app.get("/")
def index():
  return {"name":"First data"}


#path parameter

@app.get("/get-student/{student_id}")
def get_student(student_id:int=Path(None,description="The id of the student you want to view",gt=0)):
  return students[student_id]


@app.get("/hello")
def hello():
    return {"message": "hello"}