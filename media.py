import webbrowser

class Movie():
    def __init__(self, movie_title, movie_director, movie_starring, poster_image, trailer_youtube, release_date):
        self.title = movie_title
        self.director = movie_director
        self.starring = movie_starring
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)