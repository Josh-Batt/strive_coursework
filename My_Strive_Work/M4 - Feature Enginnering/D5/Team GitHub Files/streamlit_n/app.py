"""Main module for the streamlit app"""
import streamlit as st
import home
import finder_galx
import preprocessing
import about


st.markdown(
    """
    <style>
     .main {
     # background-color: #0d0e12;

     }
    </style>
    """,
    unsafe_allow_html=True
)


def main():

    PAGES = {
        "Home": home,
        "Preprocessing": preprocessing,
        "Finder": finder_galx,
        "About us ": about

    }
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()


if __name__ == "__main__":
    main()
