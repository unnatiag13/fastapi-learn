from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"))

cur = conn.cursor()

# cur.execute("SELECT * FROM movies")

# records = cur.fetchall()

app = FastAPI()

class Movies(BaseModel):
    name : str
    is_watched : bool | None = None

movies_list =[]

@app.get("/movies/")
def get_movies():
    cur.execute("SELECT * FROM movies")
    fetched_movies = cur.fetchall()
    return fetched_movies


@app.get("/movies/{serial_no}")
def get_movie(serial_no:int):
    cur.execute("SELECT name FROM movies WHERE serial_no= %s",(serial_no,))
    fetched_movie = cur.fetchall()
    return fetched_movie

@app.post("/movies/")  
def create_movie_list(movie:Movies):
    cur.execute("INSERT INTO movies(name,is_watched) VALUES (%s,%s) ",(movie.name,movie.is_watched))
    conn.commit()
    return "Movie added successfully!"
