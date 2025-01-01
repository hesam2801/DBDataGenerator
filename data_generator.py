import itertools
import datetime
import json
import numpy as np 
import sqlite3
import random

with open("data/names/first-names.txt", "r") as f1:
    names_file = f1.read()

names = names_file.split()

with open("data/names/first-names.txt", "r") as f2:
    families_file = f2.read()

families = families_file.split()

# names and families
names_families_combo = list(itertools.product(names, families))

with open("data/countries/countries.txt") as f3:
    countries_file = f3.read()

# countries
countries = countries_file.split()

year = datetime.datetime.today().year

# years
years = [year - i for i in range(35)]

with open("data/genres/genres.json") as f4:
    # genres
    genres = json.loads(f4.read())

# ratings
ratings = list(np.arange(1, 5.5, .5))

with open("data/movies/movie_list.txt") as f5:
    movies_file = f5.read()

movies_choices = movies_file.split()[:1000]

movies_combo = list(itertools.combinations(movies_choices, 2))

# movies
movies = [movie[0] + " " + movie[1] for movie in movies_combo]

words_choices = []
with open("data/words/wiki-100k.txt", encoding="utf-8") as f6:
    words_file = f6.read().split("\n")
    for word in words_file:
        if "#!comment:" not in word:
            words_choices.append(word)

descriptions = []
words_1 = list(itertools.combinations(words_choices[:100], 4))
descriptions_1 = [word[0] + " " + word[1] + " " +
                  word[2] + " " + word[3] for word in words_1]
words_2 = list(itertools.combinations(words_choices[100:200], 4))
descriptions_2 = [word[0] + " " + word[1] + " " +
                  word[2] + " " + word[3] for word in words_2]
words_3 = list(itertools.combinations(words_choices[200:300], 4))
descriptions_3 = [word[0] + " " + word[1] + " " +
                  word[2] + " " + word[3] for word in words_3]
descriptions.extend(descriptions_1)
descriptions.extend(descriptions_2)
descriptions.extend(descriptions_3)


cnn = sqlite3.connect("db.sqlite3")
cur = cnn.cursor()


for i in range(10000):
    actor_name_index = random.randint(0, len(names)-1)
    actor_name = names[actor_name_index]
    actor_family_index = random.randint(0, len(families)-1)
    actor_family = families[actor_family_index]
    actor_born_index = random.randint(0, len(years)-1)
    actor_born = years[actor_born_index]
    a = f"INSERT INTO actors (`firstname`, `lastname`, `born_year`) VALUES ('{actor_name.replace("'" , "")}', '{actor_family.replace("'" , "")}', '{actor_born}')"
    print(a)
    cur.execute(a)
    cnn.commit()

    director_name_index = random.randint(0, len(names)-1)
    director_name = names[director_name_index]
    director_family_index = random.randint(0, len(families)-1)
    director_family = families[director_family_index]
    director_born_index = random.randint(0, len(years)-1)
    director_born = years[director_born_index]
    b = f"INSERT INTO directors (`firstname`, `lastname`, `born_year`) VALUES ('{director_name.replace("'" , "")}', '{director_family.replace("'" , "")}', '{director_born}')"
    print(b)
    cur.execute(b)
    cnn.commit()


for i in range(len(countries)):
    country = countries[i]
    a = f"INSERT INTO countries (`name`) VALUES ('{country.replace("'" , "")}')"
    print(a)
    cur.execute(a)
    cnn.commit()


for i in range(len(genres)):
    genre = genres[i]
    a = f"INSERT INTO genres (`title`) VALUES ('{genre.replace("'" , "")}')"
    print(a)
    cur.execute(a)
    cnn.commit()

for i in range(len(movies)):
    movie = movies[i]
    description_index = random.randint(0, len(descriptions)-1)
    description = descriptions[description_index]
    year = random.randint(0, len(years)-1)
    rating = random.randint(0, len(ratings)-1)
    a = f"INSERT INTO movies (`title`, `description`, `year`, `rating`) VALUES ('{movie.replace("'" , "")}', '{description.replace("'" , "")}', '{year}', '{rating}')"
    print(a)
    cur.execute(a)
    cnn.commit()


for i in range(1, len(movies)):
    actrs = set( random.choices(list(range(1, 10000)), k=random.randint(5,15)))
    for actr in actrs:
        a = f"INSERT INTO movies_actors (`movie_id`, `actor_id`) VALUES ('{i}', '{actr}')"
        print(a)
        cur.execute(a)
        cnn.commit()


for i in range(1, len(movies)):
    drcts = set( random.choices(list(range(1, 10000)), k=random.randint(2,5)))
    for drct in drcts:
        a = f"INSERT INTO movies_directors (`movie_id`, `director_id`) VALUES ('{i}', '{drct}')"
        print(a)
        cur.execute(a)
        cnn.commit()


for i in range(1, len(movies)):
    gnrs = set( random.choices(list(range(1, len(genres))), k=random.randint(3,5)))
    for gnr in gnrs:
        a = f"INSERT INTO movies_genres (`movie_id`, `genre_id`) VALUES ('{i}', '{gnr}')"
        print(a)
        cur.execute(a)
        cnn.commit()

for i in range(1, len(movies)):
    cntrs = set( random.choices(list(range(1, len(countries))), k=random.randint(5, 10)))
    for cntr in cntrs:
        amount = random.randint(100000000, 1000000000)
        a = f"INSERT INTO sales (`amount`, `country_id`, `movie_id`) VALUES ({amount}, '{cntr}', '{i}')"
        print(a)
        cur.execute(a)
        cnn.commit()
    