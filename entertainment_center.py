import media
import fresh_tomatoes

# 'media.py' and 'fresh_tomatoes.py' files must be in the same directory with
# the'entertainment_center.py' file.
# Also, the images for two movies (lifeofpi.jpg and TheIntouchables.jpg)
# must be in the same folder with 'entertainment_center.py' and
# 'media.py' and 'fresh_tomatoes.py' files (I could not find good links
# for them).

# Defining four Movie objects; Movie class is defined in 'media' module
life_of_pi = media.Movie("Life Of Pi",
                         "A story of a boy and a tiger in the ocean",
                         "LifeOfPi.jpg",
                         "https://www.youtube.com/watch?v=3mMN693-F3U")

the_intouchables = media.Movie("The Intouchables",
                               "A man-nurse of a sick man helps the patient siritually",  # noqa
                               "TheIntouchables.jpg",
                               "https://www.youtube.com/watch?v=34WIbmXkewU")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

nu_pogodi = media.Movie("Nu Pogodi",
                        "A favorite childrens' cartoon in Russia",
                        "https://upload.wikimedia.org/wikipedia/commons/2/2b/Nu%2C_pogodi%21_logo.png",  # noqa
                        "https://www.youtube.com/watch?v=fZTBffmVWeE")

# Creating a list of Movie objects from the four individual Movie objects
movies = [life_of_pi, the_intouchables, avatar, nu_pogodi]

# Calling the function open_movies_page defined in 'fresh_tomatoes.py' file.
# This function creates the html file with all the movies and
# opens it in a browser.
fresh_tomatoes.open_movies_page(movies)
