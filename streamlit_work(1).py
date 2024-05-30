import streamlit as st
from streamlit_space import space
import plotly.express as px
import pandas as pd
import seaborn as sb
import numpy as np
with st.sidebar:
    st.markdown("Author: **Le Phuong**")
    st.text("Description: This is my Interactive Web Application for Python Project 2.")
st.title("Business IT 2|Python") 
st.markdown("IMDB Top 250 Movies")
st.divider()
df = pd.read_csv('IMDB Top 250 Movies.csv')
drama_df = df[df['genre'] == 'Drama']
st.markdown(
"""
- **Description**:IMDB is a large online movie-database
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
    8. **tagline**: Tagline of the movie
    9. **budget**: Budget of the movie (dollars)
    10. **box_office**: Total box office collection across the world (dollars)
    11. **casts**: All casts of the movie
    12. **directors**: Director of the movie
    13. **writers**: Writer of the movie
"""
)
tab1= st.tabs(["General relation"])
with tab1:
    col1, col2 = st.columns([1,3])
    with col1:
        space(lines=10)
        by_what = st.radio(
            "Choose a certificate:",
            ('R', '18+', 'Unrated', 'Not Rated', 'PG-13','Passed'),
            key = "r1")
    with col2:
 g=sb.FacetGrid(data=drama_df, col="certificate", col_wrap=3, sharex=False)
certificates = drama_df['certificate'].unique()
palette = sb.color_palette("husl", len(certificates))

for i, certificate in enumerate(certificates):
    subset_df = drama_df[drama_df['certificate'] == certificate]
   px.violin(x="rating", data=subset_df,color=palette[i],ax=g.axes[i],cut=0, inner= None)

g.set_titles(col_template="{col_name}")
for ax in g.axes.flat:
    ax.set_xlabel("Rating")
    ax.set_xticks(np.arange(8.1,9.3,0.2))

g.fig.subplots_adjust(top=0.9, wspace=0.5, hspace=0.5)
g.fig.suptitle("Rating & Certificate among Drama Movies", fontsize=16, fontweight= 'bold')
st.pyplot(g.fig)
