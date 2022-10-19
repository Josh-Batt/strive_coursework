import streamlit as st
# import streamlit as st
# import pandas as pd
# import matplotlib as plt
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
from PIL import Image
# import plotly.express as px
# import plotly.figure_factory as ff


def app():

    header = st.beta_container()
    team = st.beta_container()
    activities = st.beta_container()
    github = st.beta_container()
    # dataset = st.beta_container()
    # conclusion = st.beta_container()
    # footer = st.beta_container()
    with header:
        st.title('Leia Team ')  # site title h1
        st.text(' ')
        st.header('Find the Beby Yoda in Galaxy Project')

        st.text(' ')
        st.markdown(
            "Enjoy the journey and you'll see the magic :sparkles:")
        st.text(' ')

        image = Image.open('images/star-wars-leia.jpg')
        st.image(image, caption="'It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.'")
        st.text(' ')
        with team:
            st.header('Team')
            col1, col2, col3, col4 = st.beta_columns(4)
            with col1:
                image = Image.open('images/than.jpg')
                st.image(image, caption="")
                st.markdown(
                    '[Thanh Nguyen](https://github.com/fistadev)')
            with col2:
                image = Image.open('images/josha.jpeg')
                st.image(image, caption="")
                st.markdown(
                    '[Joshua Batt](https://github.com/AgathiyaRaja)')
            with col3:
                image = Image.open('images/Dilan.jpeg')
                st.image(image, caption="")
                st.markdown(
                    '[Udawala_Hewage_Dil](https://github.com/avocami)')
            with col4:
                image = Image.open('images/nurlan.jpeg')
                st.image(image, caption="")
                st.markdown(
                    '[Nurlan Sarkhanov](https://github.com/nsarkhanov)')
            st.text(' ')
            st.text(' ')
            image = Image.open('images/galaxy.jpg')
            st.image(image, caption="")
            st.text(' ')
            st.text(' ')

    with activities:
        # activities section:
        st.header('Activities')
        st.markdown('* Reading data from csv file ')
        st.markdown('* Find the Planet form  Pakanets list')
        st.markdown('* Creating costum function  ')
        st.markdown('* Find location of Beby Yoda ')
        st.text(' ')

    with github:
        # github section:
        st.header('GitHub / Instructions')
        st.markdown(
            'Check the instruction [here](https://github.com/Leia-Team/leia_team.io)')
        st.text(' ')
