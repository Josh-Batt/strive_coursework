import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
import plotly.express as px
import plotly.figure_factory as ff


def load_data(type):
    if type == "galaxy":
        data = pd.read_csv("./data/galaxies.csv")
        return data
    elif type == "planet":
        data = pd.read_csv("./data/planet.csv")
        return data


def app():

    header = st.beta_container()
    body = st.beta_container()
    activities = st.beta_container()
    github = st.beta_container()
    # dataset = st.beta_container()
    # conclusion = st.beta_container()
    # footer = st.beta_container()
    with header:
        st.title('Preprocessing Galaxy-data')  # site title h1
        st.text(' ')

        st.text(' ')
        st.markdown(
            "Lets check data in galaxy file :sparkles:")
        st.text(' ')

# Load 10,000 rows of data into the dataframe.
        data = load_data("galaxy")
        data_load_state = st.text('Loading data...')
        st.write(data.head(10))
        # Notify the reader that the data was successfully loaded.
        data_load_state.text('Loading data...done!')
        st.text(' ')
        with body:

            st.title('Procedures')
            st.markdown(
                '* Create model  with 3 clusters  KMeans adn fit the model   ')
            st.markdown('* Find  Clusters')
            st.markdown('* Separete  cluster from each other  ')
            st.markdown('* Make a scatter plot to see ')
            st.text(' ')
            st.subheader('                                      All galaxy ')
            image = Image.open('./graphics/gaalxy_all.png')
            st.image(image, caption="")
            st.header('* What is next ')
            st.markdown(
                "![Alt Text](https://media.giphy.com/media/xT39D7FdPu6Epy2PGo/giphy.gif)")
            st.markdown('* Find the planet where the most righ  side ')
            st.markdown('* We find the planet ')
            image = Image.open('./graphics/beby.png')
            st.image(image, caption="")
            st.markdown("* Let's go")
            st.markdown(
                "![Alt Text](https://media.giphy.com/media/3ohzdUihJNqMBX3efK/giphy.gif)")
#
