from imports import *
import streamlit as st
from streamlit.connections import SQLConnection
from sqlalchemy import text

conn = st.connection('movie_main', type='sql')

with conn.session as s:
   s.execute(text("create table if not exists movies(title varchar, genre varchar, director varchar, cast varchar, plot varchar, primary key(title))"))

dataset = pd.read_csv('clean_dataset.csv')

dataset_len = len(dataset['title'])

for i in range(dataset_len):

    opening_titles = dataset['title'].values[i]
    factions = dataset['genres'].values[i]
    the_director = dataset['director'].values[i]
    star_studded_cast = dataset['cast'].values[i]
    the_plot_thickens = dataset['overview'].values[i]

    try:
        with conn.session as s:
            s.execute(text("INSERT INTO movies VALUES (:title, :genre, :director, :cast, :plot)"), params = {'title': opening_titles, 'genre': factions, 'director':  the_director, 'cast' : star_studded_cast, 'plot' : the_plot_thickens})
            s.commit()
    except Exception as e:
        print(e)

s.close()


    