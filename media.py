import webbrowser
class Movie():
    def __init__(svetlana, movie_title, movie_storyline, poster_image, trailer_youtube):
        svetlana.title=movie_title
        svetlana.storyline =movie_storyline
        svetlana.poster_image_url=poster_image
        svetlana.trailer_youtube_url=trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
