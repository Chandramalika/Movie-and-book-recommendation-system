import streamlit as st
from multiapp import MultiApp
from apps import Movies,Books # import your app modules here

app = MultiApp()

st.header(""" Reccomendation App """)

app.add_app("Movies", Movies.app)
app.add_app("Books", Books.app)

# The main app
app.run()
