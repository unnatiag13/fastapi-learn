from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Student(BaseModel):
    name: str
    roll: int
    is_pass: bool | None = None


@app.get("/")
def root():
    return {"hello":"world"}

@app.get("/students/{Student_id}")
def read_students(Student_id:int , q :str):
    return {"Student ID":Student_id, "q":q}

@app.put("/students/{Student_id}")
def update_students(Student_id:int,student:Student):
    return {"Student_name":student.name,"Student_roll":student.roll ,"Student_id": Student_id}


@app.post("/students/")
def create_students(student:Student):
    return student.roll