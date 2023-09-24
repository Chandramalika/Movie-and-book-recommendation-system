import pickle
import streamlit as st
import requests
import pandas as pd

def app():
    def recommend(movie):
        index = movies[movies['Title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        for i in distances[1:11]:
            
            recommended_movie_names.append(movies.iloc[i[0]].Title)

        return recommended_movie_names
    st.header('Movie Recommendations')
    movie_dict = pickle.load(open(r'apps\movies.pkl','rb'))
    movies=pd.DataFrame(movie_dict)
    similarity = pickle.load(open(r'apps\similarity.pkl','rb'))

    movie_list = movies['Title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    if st.button('Show Recommendation'):
        recommended_movie_names = recommend(selected_movie)
        
        for i in range(10):
            st.text(recommended_movie_names[i])
        