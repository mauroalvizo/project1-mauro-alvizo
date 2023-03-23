from flask import Flask
import requests
import json
from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())

def random_movie_selector():
    import random
    #Puss n Boots = 315162
    #Spiderverse = 324857
    #Shawkshank Redemption = 278
    movie_numbers = [315162, 324857, 278]
    random_movie_number = random.choice(movie_numbers)
    return random_movie_number


def grab_bulk_movie_data():
    TMDB_PATH_URL = "https://api.themoviedb.org/3/movie/"
    movie_id = str(random_movie_selector())
    movie_data = requests.get(
            TMDB_PATH_URL + movie_id,
            params={
                "api_key": getenv("TMDB_API_KEY"),
            },
        )
    
    movie_data_list = movie_data.json()["title"]
    print(movie_data_list)
    
    return movie_data

    
app = Flask(__name__)

@app.route('/')
def test():
    
    #reminder: once this command runs you must use this instance to get the correct random movie
    movie_data = grab_bulk_movie_data()
    
    movie_name = movie_data.json()["title"]
    movie_genre = [genre["name"] for genre in movie_data.json()["genres"]]
    movie_tagline = movie_data.json()["tagline"]
    
    
    movie_image = movie_data.json()["poster_path"]
    BASE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
    completed_image_URL = BASE_IMAGE_URL + movie_image
    
    
    return f'Random Movie Data: TITLE = {movie_name}   GENRE = {movie_genre}   IMAGEURL = {completed_image_URL}    TAGLINE = {movie_tagline}'



