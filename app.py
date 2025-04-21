import streamlit as st
from src.recommend import recommend_book, book_names

# Set page config
st.set_page_config(page_title="Book Recommender", layout="wide")

# Sidebar branding
st.sidebar.markdown("### 👨‍💻 Shashi Sharma")
st.sidebar.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/mleshashi/)")
st.sidebar.markdown("---")

# UI
st.header('📚 Book Recommender System Using Machine Learning')

selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    book_names
)

if st.button('Show Recommendation'):
    recommended_books, poster_url = recommend_book(selected_books)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(recommended_books[i+1])
            st.image(poster_url[i+1])

