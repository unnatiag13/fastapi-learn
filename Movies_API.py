from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Movies(BaseModel):
    name : str
    is_watched : bool | None = None
    serial_no: int

movies_list =[]

@app.get("/")
def home(movie_no:int):
    return movie_no

@app.get("/movies/{movie_no}")
def get_movie(movie_no:int):
        # movie_details = movies_list[movie_no]
    found=0
    for m in movies_list:
        if(m.serial_no==movie_no):
            movie_details = m
            found=1
            break
    if(found==0):
        movie_details = "Sorry! movie not available"
    return {"Movie_no":movie_no,"movie":movie_details}

@app.put("/movies/{serial_no}")
def update_movies(serial_no:int,name:str,is_watched:bool = False):
    for m in movies_list:
        if m.serial_no == serial_no:
            m.name = name
            m.is_watched = is_watched
    return {"Serial_no":serial_no, "Name":name, "is_watched":is_watched}

@app.post("/movies/")  
def create_movie_list(movie:Movies):
    movies_list.append(movie)
    return movies_list
