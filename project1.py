from flask import Flask
from flask import Flask, request
import flask
import requests
import json
from dotenv import load_dotenv, find_dotenv
from os import getenv
import random

load_dotenv(find_dotenv())

def random_movie_selector():
    #Puss n Boots = 315162
    #Spiderverse = 324857
    #Shawkshank Redemption = 278
    #American Psyco = 1359
    #Pokemon = 39057
    movie_numbers = [315162, 324857, 278, 1359, 39057, 497, 13]
    random_movie_number = random.choice(movie_numbers)
    return random_movie_number

def random_color_selector():  
    color_code_list = ['#4b586e', '#7ba3e3', '#a38dba', '#6e2d46', '#e0dfa8', '#ab4b22', '#5ebdb6']
    random_color = random.choice(color_code_list)
    
    return random_color

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

    
app = flask.Flask(__name__)
@app.route('/about_page')
def about_page():
    background_color = random_color_selector()
    return flask.render_template("about_page.html", background_color=background_color)
    
    
@app.route('/')
def index():
    
    #reminder: once this command runs you must use this instance to get the correct random movie
    movie_data = grab_bulk_movie_data()
    
    movie_name = movie_data.json()["title"]
    movie_genre = [genre["name"] for genre in movie_data.json()["genres"]]
    movie_tagline = movie_data.json()["tagline"]
    
    background_color = random_color_selector()
    
    movie_image = movie_data.json()["poster_path"]
    BASE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
    completed_image_URL = BASE_IMAGE_URL + movie_image
    
    return flask.render_template("index.html", movie_name=movie_name, movie_genre=movie_genre, movie_tagline=movie_tagline, completed_image_URL=completed_image_URL, background_color=background_color)
    
   # return f'Random Movie Data: TITLE = {movie_name}   GENRE = {movie_genre}   IMAGEURL = {completed_image_URL}    TAGLINE = {movie_tagline}'

