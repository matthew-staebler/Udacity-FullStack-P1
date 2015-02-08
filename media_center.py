import urllib
import movie
import imdb_parser
import fresh_tomatoes
import json
import os

"""
Build a Movie object wiht information scraped from IMDB.
    imdb_id - ID of the movie on IMDB
    youtube_url - URL of the movie trailer on youtube
"""
def build_movie(imdb_id, youtube_url):
    imdb_content = urllib.urlopen("http://www.imdb.com/title/" + imdb_id).read()
    parser = imdb_parser.IMDBParser()
    parser.feed(imdb_content)
    return movie.Movie(parser.title, parser.storyline, parser.poster_url, youtube_url)

"""
Load the movies to include on the trailer website from the specified file.
    file_name - name of the file from which to get the movies
"""
def load_movies_from_json(file_name):
    movies_file = open(file_name)
    movies_as_json = json.load(movies_file)
    movies_file.close()
    return movies_as_json

movies = []
movies_as_json = load_movies_from_json("movies.json")
for movie_as_json in movies_as_json:
    movies.append(build_movie(movie_as_json['IMDB id'], movie_as_json['trailer url']))
fresh_tomatoes.open_movies_page(movies)
