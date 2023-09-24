import pickle
import streamlit as st
import requests
import pandas as pd

def app():
    def recommend(book):
        index = books[books['title'] == book].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_book_names = []
        
        for i in distances[1:11]:
            
            recommended_book_names.append(books.iloc[i[0]].title)

        return recommended_book_names
    st.header('Book Recommendations')
    book_dict = pickle.load(open(r'apps\books.pkl','rb'))
    books=pd.DataFrame(book_dict)
    similarity = pickle.load(open(r'apps\similarity.pkl','rb'))

    book_list = books['title'].values
    selected_book = st.selectbox(
        "Type or select a book from the dropdown",
        book_list
    )

    if st.button('Show Recommendation'):
        recommended_book_names = recommend(selected_book)
        #col1, col2, col3, col4, col5 = st.columns(5)
        for i in range(10):
            st.text(recommended_book_names[i])
        


