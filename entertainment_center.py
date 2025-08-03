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
the_odyssey = media.Movie("The Odyssey",
                        "Directed by Christopher Nolan",
                        "Starring: Matt Damon, Anne Hathaway",
                        "https://upload.wikimedia.org/wikipedia/en/9/90/The_Odyssey_%282026_film%29_poster.jpg",
                        "https://www.youtube.com/watch?v=5yzxVnFf7bE",
                        "July 17th, 2026")

the_running_man = media.Movie("The Running Man",
                      "Directed by Edgar Wright",
                      "Starring: Glen Powell, William H Macy",
                      "https://upload.wikimedia.org/wikipedia/en/4/49/The_Running_Man_2025_poster.jpg",
                      "https://www.youtube.com/watch?v=KD18ddeFuyM",
                      "November 7th, 2025")

eddington = media.Movie("Eddington",
                            "Directed by Ari Aster",
                            "Starring: Joaquin Pheonix, Pedro Pascal",
                            "https://upload.wikimedia.org/wikipedia/en/2/25/Eddington_poster.jpg",
                            "https://www.youtube.com/watch?v=oL6jZqExlIk",
                            "July 18th, 2025")

stop_making_sense = media.Movie("Stop Making Sense",
                                       "Directed by Jonathon Demme",
                                       "Starring: David Byrne",
                                       "https://upload.wikimedia.org/wikipedia/en/4/4e/Stop_making_sense_poster_original.jpg",
                                       "https://www.youtube.com/watch?v=-rjMwSTeVeo&list=RD-rjMwSTeVeo&start_radio=1",
                                       "September 23rd, 2023")

project_hail_mary = media.Movie("Project Hail Mary",
                          "Directed by Phil Lord and Christopher Miller",
                          "Starring: Ryan Gosling",
                          "https://upload.wikimedia.org/wikipedia/en/3/3b/Project_Hail_Mary_poster.jpg",
                          "https://www.youtube.com/watch?v=m08TxIsFTRI",
                          "March 20, 2026")

tron_ares = media.Movie("Tron: Ares",
                           "Directed by Joachim Rønning",
                           "Starring: Jared Leto, Greta Lee",
                           "https://upload.wikimedia.org/wikipedia/en/0/06/Tron_Ares_poster.jpg",
                           "https://www.youtube.com/watch?v=YShVEXb7-ic",
                           "October 10th, 2025")

american_sweatshop = media.Movie("American Sweatshop",
                               "Directed by Uta Briesewitz",
                               "Starring: Lili Reinhart",
                               "https://upload.wikimedia.org/wikipedia/en/4/40/American_Sweatshop_poster.jpg", 
                               "https://www.youtube.com/watch?v=ZhOUqeKL0Kg",
                               "September 19th, 2025")

ballerina = media.Movie("Ballerina",
                            "Directed by Len Wiseman",
                            "Starring: Ana de Armas",
                            "https://upload.wikimedia.org/wikipedia/en/f/f6/Ballerina_%282025_film%29_poster.jpg",
                            "https://www.youtube.com/watch?v=0FSwsrFpkbw",
                            "June 6th, 2025")

nobody_2 = media.Movie("Nobody 2",
                     "Directed by Timo Tjahjanto",
                     "Starring: Bob Odenkirk",
                     "https://upload.wikimedia.org/wikipedia/en/9/95/Nobody_2_Official_Poster.jpg",
                     "https://www.youtube.com/watch?v=-5X2pt95cIo",
                     "August 15th, 2025")

# Create list of all movies
movies = [
    the_odyssey,
    the_running_man,
    eddington,
    stop_making_sense,
    project_hail_mary,
    tron_ares,
    american_sweatshop,
    ballerina,
    nobody_2,
]

# Generate the movie trailer website
if __name__ == "__main__":
    fresh_tomatoes.open_movies_page(movies)
