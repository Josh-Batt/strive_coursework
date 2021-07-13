import streamlit as st
from preprocessing import load_data
# import pandas as pd
# import matplotlib as plt
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
from PIL import Image
# import plotly.express as px
# import plotly.figure_factory as ff


def app():
    st.title('Finder')
    step1 = st.button('Did you get the Coordinate?', key=1)
    step2 = st.button('Checking the Coordinate', key=2)
    step3 = st.button('Processing', key=3)
    step4 = st.button('Finding Place of ..', key=4)
    if step1:

        st.markdown(
            "![Alt Text](https://media.giphy.com/media/4I72kivfGWFDi3Yhkc/giphy.gif)")
        st.markdown(
            "<h3 style='text-align: center; color: red;'>Coordinate :  9.16085726217318 <------> 8.807258629151487</h3>", unsafe_allow_html=True,)
    if step2:

        st.markdown(
            "![Alt Text](https://media.giphy.com/media/4PWnEOqI4DsgA699ix/giphy.gif)")
        data = load_data("planet")
        st.subheader('Look at the Data')
        data_load_state = st.text('Loading data...')
        st.write(data.head(10))
        # Notify the reader that the data was successfully loaded.
        data_load_state.text('Loading data...done!')

    if step3:
        st.header('Procedures')
        st.markdown('* Find the point  form  locations list')
        st.markdown(
            '* Creating model, fit it, finding mean values of coordinates')
        st.markdown('* Show  the location in map ')
        st.text(' ')
        st.subheader("Locations in the map")
        image = Image.open('./graphics/map.png')
        st.image(image, caption="Yoda is  at one of them ")
        st.text(' ')
        st.markdown(
            "![Alt Text](https://media.giphy.com/media/c20UV66B7zCWA/giphy.gif)")
    if step4:
        st.header('Finally')
        st.markdown('* Where  is the little Baby ')
        st.text(' ')

        image = Image.open('./graphics/pla.png')
        st.image(image, caption="Do you see ?")
        st.text(' ')
        st.markdown(
            "![Alt Text](https://media.giphy.com/media/YTPO05SueTPez1Lr99/giphy.gif)")
        st.balloons()
