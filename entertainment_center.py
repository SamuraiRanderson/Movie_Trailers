import fresh_tomatoes
import media

nice_guys = media.Movie("The Nice Guys",
                        "A private eye investigates the apparent suicide of a fading porn star in 1970s Los Angeles and uncovers a conspiracy.",
                        "https://upload.wikimedia.org/wikipedia/en/e/e9/The_Nice_Guys_poster.png",
                        "https://www.youtube.com/watch?v=-rBp6g9criY",
                        "May 20th, 2016")

suicide_squad = media.Movie("Suicide Squad",
                            "A secret government agency recruits imprisoned supervillains to execute dangerous black ops missions in exchange for clemency.",
                            "http://static.srcdn.com/slir/w690-h1024-q90-c690:1024/wp-content/uploads/suicide-squad-poster-sweet.jpg",
                            "https://www.youtube.com/watch?v=PLLQK9la6Go",
                            "August 5th, 2016")
#print(toy_story.storyline)
knight_of_cups = media.Movie("Knight of Cups",
                            "A writer indulging in all that Los Angeles and Las Vegas has to offer undertakes a search for love and self via a series of adventures with six different women.",
                            "https://upload.wikimedia.org/wikipedia/en/c/c4/Knight_of_Cups_poster.jpg",
                            "https://www.youtube.com/watch?v=SI2j1FHCjtM",
                             "March 4th, 2016")
#print(avatar.storyline)
#avatar.show_trailer()
alice = media.Movie("Alice Through the Looking Glass",
                    "Alice returns to the whimsical world of Wonderland and travels back in time to save the Mad Hatter.",
                    "https://upload.wikimedia.org/wikipedia/en/b/b4/Alice_Through_the_Looking_Glass_%28film%29_poster.jpg",
                    "https://www.youtube.com/watch?v=OiEG3Zr_Jxs",
                    "May 27th, 2016")

fantastic = media.Movie("Fantastic Beasts and Where to Find Them",
                        "The adventures of writer Newt Scamander in New York's secret community of witches and wizards seventy years before Harry Potter reads his book in school.",
                        "https://upload.wikimedia.org/wikipedia/en/5/5e/Fantastic_Beasts_and_Where_to_Find_Them_poster.png",
                        "https://www.youtube.com/watch?v=Wj1devH5JP4",
                        "Novemeber 18th, 2016")

high_rise = media.Movie("High-Rise",
                        "Life for the residents of a tower block begins to run out of control.",
                        "https://upload.wikimedia.org/wikipedia/en/f/f5/High_Rise_2014_Film_Poster.jpg",
                        "https://www.youtube.com/watch?v=9dPp1PmNc5M",
                        "May 13th, 2016")

movies = [nice_guys, suicide_squad, knight_of_cups, alice, fantastic, high_rise]
fresh_tomatoes.open_movies_page(movies)
