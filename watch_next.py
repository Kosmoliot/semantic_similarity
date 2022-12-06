#====Import====#
import spacy


#====Global variables====#
user_movie = """
Will he save their world or destroy it? When the Hulk becomes too dangerous
for the Earth, the Illuminati trick Hulk in to a shuttle and launch him into
space to a planet where the Hulk can live in peace. Unfortunately, Hulk land 
on the planet Sakaar where he is sold into slavery and trained as agladiator."""

nlp = spacy.load('en_core_web_md')
movie_nlp = nlp(user_movie)
movie_data = {}


#====Functions====#
# Func will read movies from the file with their discription, split the text into 
# 'name' and 'description' which will be saved as key value pair in a 'movie_data' 
# dictionary. Will habdle an error if file doesn't exist.
def read_file():
    try:
        movies = open('movies.txt', 'r')
        for line in movies.readlines():
            line = line.strip('\n').split(':')
            movie_data[line[0]] = nlp(line[1])
    except FileNotFoundError:
        print("Couldn't compare any movies, no database.")
    finally:
        if movies is not None:
            movies.close()


# Similarity comparison function. Will compare users_movie to each movie 
# from the file and will return highest similarity score and movie index 
# in 'movie_data' dictionary.
def similar_movies():
    read_file()
    score = 0
    movie_index = 0
    for count, movie in enumerate(movie_data.values()):
        similarity = movie[0].similarity(movie_nlp)
        if similarity > score:
            score = similarity
            movie_index = count  
    return (movie_index, score)


# Will call 'similar_movies' function and print out movie name and highest score
def best_match():
    movie_index, score = similar_movies()
    movie_name = list(movie_data.keys())[movie_index]
    print("\nBest possible match is a '{}',".format(movie_name))
    print("with the highest similarity score of {}\n".format(round(score, 2)))

#====Init====#
best_match()