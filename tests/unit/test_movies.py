import pytest
import json
import src.movies
import requests_mock

def test_popular_movies():
    # api authorization since we are using mock this doesn't need to have real values in it
    headers = {
        "accept": "accept",
        "Authorization": "authorization"
    }

    # this function makes it so a call to the api using this endpoint will return this information
    # essentially we are testing the fact that the function calls the right endpoint
    with requests_mock.Mocker() as mock_requests:
        mock_requests.get("https://api.themoviedb.org/3/movie/popular?language=en-US&page=1&region=840", json={
            "page": 1,
            "results": [
                {
                    "id": 609681
                }
            ]
        }
        )
        expected = { # I think make expected the same as the mock request
            "page": 1,
            "results": [
                {
                    "id": 609681
                }
            ]
        }
        actual = src.movies.popular_movies(1, headers) # call the request with popular_movies
        assert actual == expected # if popular_movies calls the correct endpoint then our assertion will be true
    

def test_toprated_movies():
    # api authorization
    headers = {
        "accept": "accept",
        "Authorization": "authorization"
    }

    # copied the same testing style as popular movies refer to that for more detailed comments
    with requests_mock.Mocker() as mock_requests:
        mock_requests.get("https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1&region=840", json={
            "page": 1,
            "results": [
                {
                    "id": 278
                }
            ]
        }
        )
        expected = {
            "page": 1,
            "results": [
                {
                    "id": 278
                }
            ]
        }
        actual = src.movies.toprated_movies(1, headers)
        assert actual == expected


def test_extract_movie_data():
    data = {
        "page": 1,
        "results": [
            {
                "backdrop_path": "/kXfqcdQKsToO0OUXHcrrNCHDBzO.jpg",
                "genre_ids": [
                18,
                80
                ],
                "id": 278,
                "original_language": "en",
                "original_title": "The Shawshank Redemption",
                "overview": "Framed in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.",
                "popularity": 139.421,
                "poster_path": "/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
                "release_date": "1994-09-23",
                "title": "The Shawshank Redemption",
                "vote_average": 8.711,
                "vote_count": 25398
            },
            {
                "backdrop_path": "/rSPw7tgCH9c6NqICZef4kZjFOQ5.jpg",
                "genre_ids": [
                18,
                80
                ],
                "id": 238,
                "original_language": "en",
                "original_title": "The Godfather",
                "overview": "Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family. When organized crime family patriarch, Vito Corleone barely survives an attempt on his life, his youngest son, Michael steps in to take care of the would-be killers, launching a campaign of bloody revenge.",
                "popularity": 129.69,
                "poster_path": "/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
                "release_date": "1972-03-24",
                "title": "The Godfather",
                "vote_average": 8.7,
                "vote_count": 19340
            },
            {
                "backdrop_path": "/kGzFbGhp99zva6oZODW5atUtnqi.jpg",
                "genre_ids": [
                18,
                80
                ],
                "id": 240,
                "original_language": "en",
                "original_title": "The Godfather Part II",
                "overview": "In the continuing saga of the Corleone crime family, a young Vito Corleone grows up in Sicily and in 1910s New York. In the 1950s, Michael Corleone attempts to expand the family business into Las Vegas, Hollywood and Cuba.",
                "popularity": 71.736,
                "poster_path": "/hek3koDUyRQk7FIhPXsa6mT2Zc3.jpg",
                "release_date": "1974-12-20",
                "title": "The Godfather Part II",
                "vote_average": 8.6,
                "vote_count": 11667
            }
        ]
    }
        
    expected = {
        "movies": [
                {
                "id": 278,
                "title": "The Shawshank Redemption"
                },
                {
                "id": 238,
                "title": "The Godfather"
                },
                {
                "id": 240,
                "title": "The Godfather Part II"
                }
        ]
    }
    actual = src.movies.extract_movie_data(data)
    assert actual == expected

    data = {
        "page": 1,
        "results": [
            {
                "backdrop_path": "/kXfqcdQKsToO0OUXHcrrNCHDBzO.jpg",
                "genre_ids": [
                18,
                80,
                16
                ],
                "id": 278,
                "original_language": "en",
                "original_title": "The Shawshank Redemption",
                "overview": "Framed in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.",
                "popularity": 139.421,
                "poster_path": "/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
                "release_date": "1994-09-23",
                "title": "The Shawshank Redemption",
                "vote_average": 8.711,
                "vote_count": 25398
            },
            {
                "backdrop_path": "/rSPw7tgCH9c6NqICZef4kZjFOQ5.jpg",
                "genre_ids": [
                18,
                80
                ],
                "id": 238,
                "original_language": "en",
                "original_title": "The Godfather",
                "overview": "Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family. When organized crime family patriarch, Vito Corleone barely survives an attempt on his life, his youngest son, Michael steps in to take care of the would-be killers, launching a campaign of bloody revenge.",
                "popularity": 129.69,
                "poster_path": "/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
                "release_date": "1972-03-24",
                "title": "The Godfather",
                "vote_average": 8.7,
                "vote_count": 19340
            },
            {
                "backdrop_path": "/kGzFbGhp99zva6oZODW5atUtnqi.jpg",
                "genre_ids": [
                18,
                80
                ],
                "id": 240,
                "original_language": "en",
                "original_title": "The Godfather Part II",
                "overview": "In the continuing saga of the Corleone crime family, a young Vito Corleone grows up in Sicily and in 1910s New York. In the 1950s, Michael Corleone attempts to expand the family business into Las Vegas, Hollywood and Cuba.",
                "popularity": 71.736,
                "poster_path": "/hek3koDUyRQk7FIhPXsa6mT2Zc3.jpg",
                "release_date": "1974-12-20",
                "title": "The Godfather Part II",
                "vote_average": 8.6,
                "vote_count": 11667
            }
        ]
    }
        
    expected = {
        "movies": [
                {
                "id": 238,
                "title": "The Godfather"
                },
                {
                "id": 240,
                "title": "The Godfather Part II"
                }
        ]
    }

    actual = src.movies.extract_movie_data(data)
    assert actual == expected


def test_actors():
    # api authorization
    headers = {
        "accept": "accept",
        "Authorization": "authorization"
    }

    # copied the same testing style as popular movies refer to that for more detailed comments.
    with requests_mock.Mocker() as mock_requests:      
        mock_requests.get("https://api.themoviedb.org/3/movie/278/credits?language=en-US", json={
            "id": 278,
            "cast": [
                    {
                    "gender": 2,
                    "id": 504,
                    "known_for_department": "Acting",
                    "name": "Tim Robbins",
                    "original_name": "Tim Robbins",
                    "popularity": 32.322,
                    "profile_path": "/A4fHNLX73EQs78f2G6ObfKZnvp4.jpg",
                    "cast_id": 3,
                    "character": "Andy Dufresne",
                    "credit_id": "52fe4231c3a36847f800b131",
                    "order": 0
                    },
                    {
                    "gender": 2,
                    "id": 192,
                    "known_for_department": "Acting",
                    "name": "Morgan Freeman",
                    "original_name": "Morgan Freeman",
                    "popularity": 119.503,
                    "profile_path": "/jPsLqiYGSofU4s6BjrxnefMfabb.jpg",
                    "cast_id": 4,
                    "character": "Ellis Boyd 'Red' Redding",
                    "credit_id": "52fe4231c3a36847f800b135",
                    "order": 1
                    },
                    {
                    "gender": 2,
                    "id": 4029,
                    "known_for_department": "Acting",
                    "name": "Bob Gunton",
                    "original_name": "Bob Gunton",
                    "popularity": 29.707,
                    "profile_path": "/ulbVvuBToBN3aCGcV028hwO0MOP.jpg",
                    "cast_id": 5,
                    "character": "Warden Norton",
                    "credit_id": "52fe4231c3a36847f800b139",
                    "order": 2
                    },
                    {
                    "gender": 2,
                    "id": 6573,
                    "known_for_department": "Acting",
                    "name": "William Sadler",
                    "original_name": "William Sadler",
                    "popularity": 40.262,
                    "profile_path": "/rWeb2kjYCA7V9MC9kRwRpm57YoY.jpg",
                    "cast_id": 7,
                    "character": "Heywood",
                    "credit_id": "52fe4231c3a36847f800b13d",
                    "order": 3
                    },
                    {
                    "gender": 2,
                    "id": 6574,
                    "known_for_department": "Acting",
                    "name": "Clancy Brown",
                    "original_name": "Clancy Brown",
                    "popularity": 60.126,
                    "profile_path": "/9RgzFqbmWBLVfq9wvyDo5UW8VT1.jpg",
                    "cast_id": 8,
                    "character": "Captain Byron T. Hadley",
                    "credit_id": "52fe4231c3a36847f800b141",
                    "order": 4
                    },
                    {
                    "gender": 2,
                    "id": 6575,
                    "known_for_department": "Acting",
                    "name": "Gil Bellows",
                    "original_name": "Gil Bellows",
                    "popularity": 27.165,
                    "profile_path": "/eCOIv2nSGnWTHdn88NoMyNOKWyR.jpg",
                    "cast_id": 9,
                    "character": "Tommy",
                    "credit_id": "52fe4231c3a36847f800b145",
                    "order": 5
                    },
                    {
                    "gender": 2,
                    "id": 6577,
                    "known_for_department": "Acting",
                    "name": "James Whitmore",
                    "original_name": "James Whitmore",
                    "popularity": 20.057,
                    "profile_path": "/d1nOu22OvPzdwS8euWE0FNHwx8K.jpg",
                    "cast_id": 11,
                    "character": "Brooks Hatlen",
                    "credit_id": "52fe4231c3a36847f800b14d",
                    "order": 6
                    },
                    {
                    "gender": 2,
                    "id": 6576,
                    "known_for_department": "Acting",
                    "name": "Mark Rolston",
                    "original_name": "Mark Rolston",
                    "popularity": 15.239,
                    "profile_path": "/hcrNRIptYMRXgkJ9k76BlQu6DQp.jpg",
                    "cast_id": 10,
                    "character": "Bogs Diamond",
                    "credit_id": "52fe4231c3a36847f800b149",
                    "order": 7
                    }
                ]
        }
        )
        expected = {'movies': [{'id': 278, 'title': "The Shawshank Redemption", 'actors': [192, 6574, 6573, 504]}]}

        data = {
        "movies": [
                {
                "id": 278,
                "title": "The Shawshank Redemption"
                }
        ]
        }

        actual = src.movies.actors(data, headers)
        assert actual == expected


def test_popular_actors():
    # create a fake cast output from the api
    cast={
            "id": 278,
            "cast": [
                    {
                    "gender": 2,
                    "id": 504,
                    "known_for_department": "Acting",
                    "name": "Tim Robbins",
                    "original_name": "Tim Robbins",
                    "popularity": 32.322,
                    "profile_path": "/A4fHNLX73EQs78f2G6ObfKZnvp4.jpg",
                    "cast_id": 3,
                    "character": "Andy Dufresne",
                    "credit_id": "52fe4231c3a36847f800b131",
                    "order": 0
                    },
                    {
                    "gender": 2,
                    "id": 192,
                    "known_for_department": "Acting",
                    "name": "Morgan Freeman",
                    "original_name": "Morgan Freeman",
                    "popularity": 119.503,
                    "profile_path": "/jPsLqiYGSofU4s6BjrxnefMfabb.jpg",
                    "cast_id": 4,
                    "character": "Ellis Boyd 'Red' Redding",
                    "credit_id": "52fe4231c3a36847f800b135",
                    "order": 1
                    },
                    {
                    "gender": 2,
                    "id": 4029,
                    "known_for_department": "Acting",
                    "name": "Bob Gunton",
                    "original_name": "Bob Gunton",
                    "popularity": 29.707,
                    "profile_path": "/ulbVvuBToBN3aCGcV028hwO0MOP.jpg",
                    "cast_id": 5,
                    "character": "Warden Norton",
                    "credit_id": "52fe4231c3a36847f800b139",
                    "order": 2
                    },
                    {
                    "gender": 2,
                    "id": 6573,
                    "known_for_department": "Acting",
                    "name": "William Sadler",
                    "original_name": "William Sadler",
                    "popularity": 40.262,
                    "profile_path": "/rWeb2kjYCA7V9MC9kRwRpm57YoY.jpg",
                    "cast_id": 7,
                    "character": "Heywood",
                    "credit_id": "52fe4231c3a36847f800b13d",
                    "order": 3
                    },
                    {
                    "gender": 2,
                    "id": 6574,
                    "known_for_department": "Acting",
                    "name": "Clancy Brown",
                    "original_name": "Clancy Brown",
                    "popularity": 60.126,
                    "profile_path": "/9RgzFqbmWBLVfq9wvyDo5UW8VT1.jpg",
                    "cast_id": 8,
                    "character": "Captain Byron T. Hadley",
                    "credit_id": "52fe4231c3a36847f800b141",
                    "order": 4
                    },
                    {
                    "gender": 2,
                    "id": 6575,
                    "known_for_department": "Acting",
                    "name": "Gil Bellows",
                    "original_name": "Gil Bellows",
                    "popularity": 27.165,
                    "profile_path": "/eCOIv2nSGnWTHdn88NoMyNOKWyR.jpg",
                    "cast_id": 9,
                    "character": "Tommy",
                    "credit_id": "52fe4231c3a36847f800b145",
                    "order": 5
                    },
                    {
                    "gender": 2,
                    "id": 6577,
                    "known_for_department": "Acting",
                    "name": "James Whitmore",
                    "original_name": "James Whitmore",
                    "popularity": 20.057,
                    "profile_path": "/d1nOu22OvPzdwS8euWE0FNHwx8K.jpg",
                    "cast_id": 11,
                    "character": "Brooks Hatlen",
                    "credit_id": "52fe4231c3a36847f800b14d",
                    "order": 6
                    },
                    {
                    "gender": 2,
                    "id": 6576,
                    "known_for_department": "Acting",
                    "name": "Mark Rolston",
                    "original_name": "Mark Rolston",
                    "popularity": 15.239,
                    "profile_path": "/hcrNRIptYMRXgkJ9k76BlQu6DQp.jpg",
                    "cast_id": 10,
                    "character": "Bogs Diamond",
                    "credit_id": "52fe4231c3a36847f800b149",
                    "order": 7
                    }
                ]
        }
    
    # ensure the parsing is working correctly
    expected = [192, 6574, 6573, 504]
    actual = src.movies.popular_actors(cast)
    assert actual == expected


def test_actor_images():
    
    # api authorization
    headers = {
        "accept": "accept",
        "Authorization": "authorization"
    }

    with requests_mock.Mocker() as mock_requests:
        mock_requests.get("https://api.themoviedb.org/3/person/192/images", json={
            "id": 192,
            "profiles": [
                {
                "aspect_ratio": 0.667,
                "height": 2700,
                "file_path": "/jPsLqiYGSofU4s6BjrxnefMfabb.jpg",
                "vote_average": 5.326,
                "vote_count": 7,
                "width": 1800
                },
                {
                "aspect_ratio": 0.667,
                "height": 3000,
                "file_path": "/905k0RFzH0Kd6gx8oSxRdnr6FL.jpg",
                "vote_average": 5.264,
                "vote_count": 8,
                "width": 2000
                },
                {
                "aspect_ratio": 0.667,
                "height": 1920,
                "file_path": "/nhFqNPXDyWTRzHqIUqwayfvDmCn.jpg",
                "vote_average": 5.258,
                "vote_count": 6,
                "width": 1280
                },
                {
                "aspect_ratio": 0.667,
                "height": 999,
                "file_path": "/iRl1tJADZhnkTcirVm21zs8kJhH.jpg",
                "vote_average": 5.198,
                "vote_count": 7,
                "width": 666
                },
                {
                "aspect_ratio": 0.667,
                "height": 3000,
                "file_path": "/1ahENoyEgKSbRUd0IsydIff7rt1.jpg",
                "vote_average": 5.19,
                "vote_count": 5,
                "width": 2000
                },
                {
                "aspect_ratio": 0.667,
                "height": 1920,
                "file_path": "/iuX6R4Sfm6FK5nbfSQ8OgvWcOjy.jpg",
                "vote_average": 5.18,
                "vote_count": 3,
                "width": 1280
                }
            ]
        }
        )
        mock_requests.get("https://api.themoviedb.org/3/person/6574/images", json={
            "id": 6574,
            "profiles": [
                {
                "aspect_ratio": 0.667,
                "height": 1500,
                "file_path": "/9RgzFqbmWBLVfq9wvyDo5UW8VT1.jpg",
                "vote_average": 5.27,
                "vote_count": 10,
                "width": 1000
                },
                {
                "aspect_ratio": 0.667,
                "height": 750,
                "file_path": "/xjg0ZIxP0tFcEQCTeRgKxNtLdpe.jpg",
                "vote_average": 5.264,
                "vote_count": 8,
                "width": 500
                },
                {
                "aspect_ratio": 0.667,
                "height": 1500,
                "file_path": "/uzkU71DkwwRyO7qxwD0A254PjAS.jpg",
                "vote_average": 5.19,
                "vote_count": 5,
                "width": 1000
                },
                {
                "aspect_ratio": 0.667,
                "height": 900,
                "file_path": "/ekaX4du53NcOeEmce7nsk564cBZ.jpg",
                "vote_average": 5.18,
                "vote_count": 3,
                "width": 600
                },
                {
                "aspect_ratio": 0.667,
                "height": 2048,
                "file_path": "/9UwM8st1EdHIJIlJXD2N9PWA8uG.jpg",
                "vote_average": 5.146,
                "vote_count": 10,
                "width": 1365
                }
            ]
            }
        )

        expected = {'movies': [{'id': 278, 'title': "The Shawshank Redemption", 'actors': [192, 6574], 'actor_images': ["/jPsLqiYGSofU4s6BjrxnefMfabb.jpg", "/9RgzFqbmWBLVfq9wvyDo5UW8VT1.jpg"]}]}
        input = {'movies': [{'id': 278, 'title': "The Shawshank Redemption", 'actors': [192, 6574]}]}
        actual = src.movies.actor_images(input, headers)
        assert actual == expected


def test_related_movies():

    # api authorization
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWNhNjRiOGE1ZGM4OWZlNTNmNzQ5Y2I4MDAwMGIxMSIsInN1YiI6IjY1YjAwMWJhNjdiNjEzMDBlYjUzODA2MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.B5tu8C5pXbVtxrfR0aPJgqLu0povlRhuf1a8T7sWDjk"
    }
    
    input = {'movies': [{'id': 238, 'title': 'The Lord of the Rings: The Return of the King', 'actors': [110, 109, 1328, 1327], 'actor_images': ['/jPsLqiYGSofU4s6BjrxnefMfabb.jpg', '/9RgzFqbmWBLVfq9wvyDo5UW8VT1.jpg']}]}
    expected = {'movies': [{'id': 238, 'title': 'The Lord of the Rings: The Return of the King', 'actors': [110, 109, 1328, 1327], 'actor_images': ['/jPsLqiYGSofU4s6BjrxnefMfabb.jpg', '/9RgzFqbmWBLVfq9wvyDo5UW8VT1.jpg'], 'alternative_answers': {"A Passage to Middle-earth: Making of 'Lord of the Rings'", 'Film Collectibles: Capturing Movie Memories', 'Quest for the Ring', 'Ringers: Lord of the Fans', 'The Lord of the Rings: The Fellowship of the Ring', 'The Lord of the Rings: The Return of the King', 'The Lord of the Rings: The Two Towers', "The Quest Fulfilled: A Director's Vision", 'The Lord of the Rings: The Return of the King', 'The Lord of the Rings: The Fellowship of the Ring'}}]}

    actual = src.movies.related_movies(input, headers)
    assert actual == expected