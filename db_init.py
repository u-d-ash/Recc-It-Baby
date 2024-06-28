from imports import *
from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///movie_main.db')

Session = sessionmaker(bind=engine)
session = Session()

session.execute(text("create table if not exists movies(title varchar, genre varchar, director varchar, cast varchar, plot varchar, primary key(title))"))

dataset = pd.read_csv('clean_dataset.csv')

dataset_len = len(dataset['title'])

for i in range(dataset_len):

    opening_titles = dataset['title'].values[i]
    factions = dataset['genres'].values[i]
    the_director = dataset['director'].values[i]
    star_studded_cast = dataset['cast'].values[i]
    the_plot_thickens = dataset['overview'].values[i]

    try:
        session.execute(text("INSERT INTO movies VALUES (:title, :genre, :director, :cast, :plot)"), params = {'title': opening_titles, 'genre': factions, 'director':  the_director, 'cast' : star_studded_cast, 'plot' : the_plot_thickens})
        session.commit()
    except Exception as e:
        print(e)

session.close()


    