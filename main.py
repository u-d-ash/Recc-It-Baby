import streamlit as st
from functions import get_rex

st.set_page_config(layout="wide")

st.title("Word2Recc : Movie Recommendations")

st.text("Enter a movie title below and the app will recommend similar movies. Changing the weights will alter the recommendations.")

movie_name = st.text_input("Movie Title")

weight_expander = st.expander('Config Weights')

with weight_expander:

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    dir_weight = col2.select_slider("Director", [1, 2, 3, 4, 5])

    cast_weight = col4.select_slider("Cast", [1, 2, 3, 4, 5])

    genre_weight = col6.select_slider("Genre", [1, 2, 3, 4, 5])

button_clicked = st.button("SUBMIT")

if(button_clicked):

    resp, recc_list = get_rex(movie_name, dir_weight, cast_weight, genre_weight)

    if(resp == 0):
        st.write("ERROR : Movie Not Found !!")
    else:
        st.write("Here are the recommendations:")
        for i, movie in enumerate(recc_list):
            st.write(f"{i + 1}. {movie}")


