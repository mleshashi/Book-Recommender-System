import streamlit as st
from src.recommend import recommend_book, book_names

# Set page config
st.set_page_config(
    page_title="Book Recommender",
    layout="wide",  # needed for full-width margin control
)

# Inject custom CSS
st.markdown(
    """
    <style>
        .main {
            padding-left: 100px;
            padding-right: 100px;
            background-image: url("https://raw.githubusercontent.com/mleshashi/Book-Recommender-System/image/background.png");
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center top;
            background-attachment: fixed;
        }

        /* Optional: Add semi-transparent overlay for readability */
        .block-container {
            background-color: rgba(0, 0, 0, 0.85);
            padding: 2rem;
            border-radius: 10px;
        }

        /* Optional: Improve dropdown visibility */
        .stSelectbox>div>div>div>input {
            color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

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
            st.text(recommended_books[i + 1])
            st.image(poster_url[i + 1])
