"""
A Movie object is an object that represents a movie

Attributes:
    title - title of the movie
    storyline - storyline of the movie
    poster_image_url - URL of the movie poster
    trailer_youtube_url - URL of the movie trailer on youtube
"""
class Movie():
    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
