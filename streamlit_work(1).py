import streamlit as st
from streamlit_space import space
import plotly.express as px
import pandas as pd
import numpy as np
with st.sidebar:
    st.markdown("Author: **Le Phuong**")
    st.text("Description: This is my Interactive Web Application for Python Project 2.")
    st.title("Welcome!")
st.markdown("IMDB Top 250 Movies.")
st.divider()
df = pd.read_csv('IMDB Top 250 Movies.csv')
st.markdown(
"""
- **Description**: IMDB is a large online movie-database
platform that provides information on films
and television shows. It includes reviews
and ratings from users, serving as a
benchmark for a film's popularity and
success.
This dataset provides information on the
top 250 rated movies on IMDB from 1921
to 2022 and offers a glimpse into film
industry trends, such as rating patterns
and genre preferences.

- **Variables**:
    1. **rank**: Rank of the movie
    2. **name**: Name of the movie
    3. **year**: Release year
    4. **rating**: Rating of the movie
    5. **genre**: Genre of the movie
    6. **certificate**: Certificate of the movie
    7. **run_time**: Total movie run time
    8. **tagline **: Tagline of the movie
    9. **budget**: Budget of the movie (dollars)
    10. **box_office**: Total box office collection across the world (dollars)
    11. **casts**: All casts of the movie
    12. **directors**: Director of the movie
    13. **writers**: Writer of the movie
"""
)
