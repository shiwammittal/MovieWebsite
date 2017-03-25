import webbrowser

class Movie ():

    """This class provides a way to store related information of movies"""
    VALID_RATINGS = ["G","P","PG-13","R"]
    def __init__(self, movie_title, movie_summary, movie_poster_image, movie_trailer):
        self.title = movie_title
        self.storyline = movie_summary
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer
        
    def play_movie_trailer(self):
        webbrowser.open(self.movie_trailer)
