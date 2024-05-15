from src.movies import *

def hello():
    return "Hello world!"


def main():
    # number of pages of movies to get from the API. 1 page is 20 movies.
    pages = 1

    # api authorization
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWNhNjRiOGE1ZGM4OWZlNTNmNzQ5Y2I4MDAwMGIxMSIsInN1YiI6IjY1YjAwMWJhNjdiNjEzMDBlYjUzODA2MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.B5tu8C5pXbVtxrfR0aPJgqLu0povlRhuf1a8T7sWDjk"
    }

    data = toprated_movies(pages, headers) # gets movie data from the TMDB API
    data = extract_movie_data(data) # removes any animated movies from the list and any unnecessary data
    data = actors(data, headers) # adds the top actors to the json
    data = actor_images(data, headers) # adds the top actors images to the json
    data = related_movies(data, headers) # find any related movies that could be alternative answers



if __name__ == "__main__":
    main()
