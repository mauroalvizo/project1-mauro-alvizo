from flask import Flask
import requests
import json
from dotenv import load_dotenv, find_dotenv
from os import getenv

def random_movie_selector():
    import random

    movie_numbers = [1, 2, 3]
    random_movie_number = random.choice(movie_numbers)
    return random_movie_number




app = Flask(__name__)

@app.route('/')
def test():
    return 'Howdy Mauro I am so proud of you you are amazing :)'


