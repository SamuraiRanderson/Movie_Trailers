import fresh_tomatoes
import media

"""
Movie Trailer Website - Entertainment Center
This file contains all the movie objects for the 2017 movie trailers website.
Each movie is created using the media.Movie class with the following parameters:
- movie_title: The title of the movie
- movie_director: The director(s) of the movie  
- movie_starring: The main cast members
- poster_image: URL to the movie poster image
- trailer_youtube: YouTube trailer URL
- release_date: The movie's release date
"""

# Create movie objects for 2017 movies
star_wars = media.Movie("Star Wars: The Last Jedi",
                        "Directed by Rian Johnson",
                        "Starring: Mark Hamill, Carrie Fisher, Daisy Ridley",
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
                        "https://www.youtube.com/watch?v=zB4I68XVPzQ",
                        "December 15th, 2017")

dunkirk = media.Movie("Dunkirk",
                      "Directed by Christopher Nolan",
                      "Starring: Tom Hardy, Mark Rylance, Kenneth Branagh",
                      "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
                      "https://www.youtube.com/watch?v=_cmgiys2n1o",
                      "July 21st, 2017")

alien_covenant = media.Movie("Alien: Covenant",
                            "Directed by Ridley Scott",
                            "Starring: Michael Fassbender, Kathrine Waterston",
                            "https://upload.wikimedia.org/wikipedia/en/3/33/Alien_Covenant_Teaser_Poster.jpg",
                            "https://www.youtube.com/watch?v=u5KPP6lxRVg",
                            "May 12th, 2017")

pirates_of_the_caribbean = media.Movie("Dead Men Tell No Tales",
                                       "Directed by Joachim Ronning, Espen Sandberg",
                                       "Starring: Johnny Depp, Javier Bardem",
                                       "https://upload.wikimedia.org/wikipedia/en/2/21/Pirates_of_the_Caribbean%2C_Dead_Men_Tell_No_Tales.jpg",
                                       "https://www.youtube.com/watch?v=XibzC-e_s5M",
                                       "March 25th, 2017")

king_arthur = media.Movie("King Arthur",
                          "Directed by Guy Richie",
                          "Starring: Charlie Hunnam, Astrid Berges-Frisbey",
                          "https://upload.wikimedia.org/wikipedia/en/a/a4/King_Arthur_LotS_poster.jpg",
                          "https://www.youtube.com/watch?v=SX9y5JPuRHY",
                          "May 12th, 2017")

atomic_blonde = media.Movie("Atomic Blonde",
                           "Directed by David Leitch",
                           "Starring: Charlize Theron, James McAvoy",
                           "https://upload.wikimedia.org/wikipedia/en/b/b5/Atomic_Blonde_poster.jpg",
                           "https://www.youtube.com/watch?v=yIUube1pSC0",
                           "August 11th, 2017")

american_assassin = media.Movie("American Assassin",
                               "Directed by Michael Cuesta",
                               "Starring: Dylan O'Brien, Scott Adkins, Taylor Kitsch",
                               "https://upload.wikimedia.org/wikipedia/en/5/5d/American_Assassin.jpg",
                               "https://www.youtube.com/watch?v=XwHAGKxsbcg",
                               "September 15th, 2017")

thor_ragnarok = media.Movie("Thor: Ragnarok",
                            "Directed by Taika Waititi",
                            "Starring: Cate Blanchett, Chris Hemsworth",
                            "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                            "https://www.youtube.com/watch?v=v7MGUNV8MxU",
                            "November 3rd, 2017")

bright = media.Movie("Bright",
                     "Directed by David Ayer",
                     "Starring: Will Smith, Joel Edgerton",
                     "https://previews.123rf.com/images/carmendorin/carmendorin1401/carmendorin140100072/25118786-Grunge-rubber-stamps-with-text-Not-Available-and-Available-Coming-Soon-vector-illustration-Stock-Vector.jpg",
                     "https://www.youtube.com/watch?v=59uAseJFh7M",
                     "December 2017")

# Create list of all movies
movies = [
    star_wars,
    dunkirk,
    alien_covenant,
    pirates_of_the_caribbean,
    king_arthur,
    atomic_blonde,
    american_assassin,
    thor_ragnarok,
    bright,
]

# Generate the movie trailer website
if __name__ == "__main__":
    fresh_tomatoes.open_movies_page(movies)
