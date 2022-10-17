# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
            
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating
    return movie_dict

def add_to_watched(user_data, movie):

    user_data = {
        "watched": [movie] 
    }

    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": [movie] 
    }
    
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            movie_index = user_data["watchlist"].index(movie) 
            user_data["watchlist"].pop(movie_index) 
            user_data["watched"].append(movie)
    
    return user_data 

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data): 


    total = 0
    if len(user_data["watched"]) == 0:
        return total
    for movie in user_data["watched"]:
        total += movie["rating"]
    
    average = total / len(user_data["watched"]) 

    return average

def get_most_watched_genre(user_data): 

    if len(user_data["watched"]) == 0:
            return None

    genre_count = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_count.keys():
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    
    max_genre_count = 0
    most_watched_genre = ""
    for genre, count in genre_count.items():
        if count > max_genre_count:
            max_genre_count = count
            most_watched_genre = genre
    
    return most_watched_genre  
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):

    friends_watched_list = []
    user_watched_list = []
    user_unique_movies = []

    for num in range(0, len(user_data["friends"])):
        for movie in user_data["friends"][num]["watched"]:
            friends_watched_list.append(movie["title"])

    for movie in user_data["watched"]:
        user_watched_list.append(movie["title"])

    for movie in friends_watched_list: 
        if movie in user_watched_list:
            user_watched_list.remove(movie)  

    for title in user_data["watched"]:
        for num in range (0, len(user_watched_list)):
            if user_watched_list[num] in title["title"]:
                user_unique_movies.append(title)
    
    return user_unique_movies 

def get_friends_unique_watched(user_data):

    friends_watched_list = []
    user_watched_list = []
    friends_unique_movies = []

    for num in range(0, len(user_data["friends"])):
            for movie in user_data["friends"][num]["watched"]:
                friends_watched_list.append(movie["title"])

    friends_movies_no_doubles = list(set(friends_watched_list)) 

    for movie in user_data["watched"]:
        user_watched_list.append(movie["title"])

    for movie in user_watched_list: 
        if movie in friends_movies_no_doubles:
            friends_movies_no_doubles.remove(movie)

    for num in range (0, len(user_data["friends"])):
        for dictionary in user_data["friends"][num]["watched"]: 
            if dictionary["title"] in friends_movies_no_doubles and dictionary["title"] not in friends_unique_movies: 
                friends_unique_movies.append(dictionary)
        
    friends_truly_unique_movies = set() 
    friends_truly_truly_unique_movies = [] 

    for dictionaries in friends_unique_movies:
        tupled_dicts = tuple(dictionaries.items())
        if tupled_dicts not in friends_truly_unique_movies:
            friends_truly_unique_movies.add(tupled_dicts) 
            friends_truly_truly_unique_movies.append(dictionaries)
    
    return friends_truly_truly_unique_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    user_watched_list = []
    friends_watched_list = []

    for movie in user_data["watched"]:
            user_watched_list.append(movie["title"])

    for num in range(0, len(user_data["friends"])):
            for movie in user_data["friends"][num]["watched"]:
                friends_watched_list.append(movie["title"])


    friend_set = set(friends_watched_list)

    user_set = set(user_watched_list)

    friend_movie_reccs = friend_set - user_set

    friends_recommend = list(friend_movie_reccs)

    user_subscriptions = []

    for subscription in user_data["subscriptions"]: 
        user_subscriptions.append(subscription)

    friends_recommended_flicks = [] 

    for num in range(0, len(user_data["friends"])):
        for movie in user_data["friends"][num]["watched"]:
            if movie["title"] in friends_recommend and movie["host"] in user_subscriptions:
                    friends_recommended_flicks.append(movie)

    return friends_recommended_flicks

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data): 
    user_seen_movies = []
    friends_seen_movies = []
    recs_by_genre = [] 

    fav_genre = get_most_watched_genre(user_data)

    for dictionary in user_data["watched"]:
        user_seen_movies.append(dictionary["title"])

    for num in range(0, len(user_data["friends"])):
        for dictionary in user_data["friends"][num]["watched"]:
            friends_seen_movies.append(dictionary["title"])

    user_watched = set(user_seen_movies)
    friend_watched = set(friends_seen_movies)

    friends_recs = list(friend_watched - user_watched)

    for num in range(0, len(user_data["friends"])):
        for dictionary in user_data["friends"][num]["watched"]:
            if dictionary["title"] in friends_recs and dictionary["genre"] == fav_genre: 
                recs_by_genre.append(dictionary) 

    return recs_by_genre


def get_rec_from_favorites(user_data): 
    user_favs = []
    friend_movies = []

    for dictionary in user_data["favorites"]:
        user_favs.append(dictionary["title"])

    for num in range(0, len(user_data["friends"])):
        for dictionary in user_data["friends"][num]["watched"]:
            friend_movies.append(dictionary["title"])

    user_set = set(user_favs)
    friends_set = set(friend_movies)

    movies_to_watch = user_set - friends_set 

    user_fav_movies = list(movies_to_watch)

    fav_recommendations = [] 

    for dictionary in user_data["favorites"]:
        for movie in user_fav_movies: 
            if movie == dictionary["title"]:
                fav_recommendations.append(dictionary)

    return fav_recommendations




