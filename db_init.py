from imports import *

conn = sqlite3.connect('movie_main.db', check_same_thread=False)

with conn:
   conn.execute("create table if not exists movies(title varchar, genre varchar, director varchar, cast varchar, plot varchar, primary key(title))")

dataset = pd.read_csv('clean_dataset.csv')

dataset_len = len(dataset['title'])

for i in range(dataset_len):

    opening_titles = dataset['title'].values[i]
    factions = dataset['genres'].values[i]
    the_director = dataset['director'].values[i]
    star_studded_cast = dataset['cast'].values[i]
    the_plot_thickens = dataset['overview'].values[i]

    print(opening_titles)
    try:
        conn.execute("INSERT INTO movies VALUES (:title, :genre, :director, :cast, :plot)", {'title': opening_titles, 'genre': factions, 'director':  the_director, 'cast' : star_studded_cast, 'plot' : the_plot_thickens})
    except:
        print(f"sus in {opening_titles}")

conn.commit()


    