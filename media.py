import webbrowser


class Movie():
    """
      Inputs:
              None.
      Behavior:
              Constructor method for Movie class. It initializes an
              instance of Movie object with its title, storyline,
              poster image, and trailer
      Output:
              No output.
     """
    def __init__(svetlana, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        svetlana.title = movie_title
        svetlana.storyline = movie_storyline
        svetlana.poster_image_url = poster_image
        svetlana.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
          Inputs:
                  None.
          Behavior:
                  Opens a browser and plays the trailer by reading
                  the trailer_utube_url property of the instance
                  of the Movie class.
          Output:
                  No output.
        """
        webbrowser.open(self.trailer_youtube_url)
