import streamlit as st

st.title('Newton Fitness Motion Tracking')

# st.sidebar.header('Parameters')
# choice = st.sidebar.radio('Modes of motion', ['Still', 'Walking', 'Car', 'Train', 'Bus'])
# st.sidebar.slider('Time range', min_value=0, max_value=10)

# st.write(' ')
# st.write(' ')
# st.write(' ')
# st.write(' ')
# st.subheader(choice + ' Pipline accuracy')

# st.bar_chart() # Show accuracy of diffrent models for given activity

st.sidebar.header('Project Summary')
st.sidebar.text('''
1. Load in your data
2. Our model predicts if you are:
    - Still
    - Walking
    - Car
    - Bus
    - Train
3. If you are walking then we will 
   predict calories burnt
''')

st.text(' ')
st.text(' ')
st.text(' ')
st.text(' ')

st.number_input('')

# st.file_uploader('Load in your data')

st.text('Predicted activity = ') # Models predction

# IF predicted activity is walking then show this:
st.text('Walking calories burnt = ') # Calories burnt formaula