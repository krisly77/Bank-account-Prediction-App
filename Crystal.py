import pandas as pd
import numpy as np

#cities= ['london', 'stockholm', 'Paris', 'Uppsala']
#for city in cities:
#    print(city)

import streamlit as st
st.title("Hello, Arion Troops")
st.header("We have been on this journey for four months now.")
st.subheader('I am so proud of you guys!')
st.markdown('## We have only 9 superskills to go')
st.markdown('### Lets finish strong!')
st.success('The finish line is just ahead')
st.info('Remember to takebreaks and stay ahead')
st.warning('Dont forget to make progress on your platform')
st.error('If you encunter any issues, please reach out')
st.balloons()
st.snow()
exp = ZeroDivisionError('This is a zero division error example.')
st.exception(exp)

from PIL import Image
img = Image.open("C:/Users/MY LAPTOP/Pictures/Conceptual Model.png")
st.image(img, caption= 'Conceptual Model', use_container_width= True)

status = st.radio('Select Gender:', ('Male', 'Female'))

if status == 'Male':
    st.success('Male')
else:
    st.success('Female')

hobby = st.selectbox('Hobbies:', ['Reading', 'Singing', 'Crafting'])

st.write('Your hobby is: ', hobby)

hobbies = st.multiselect('Hobbies:', ['Reading', 'Singing', 'Crafting'])

st.write('You selected hobbies: ', hobbies)
st.write('You delected', len(hobbies), 'hobbies')

st.button('Click me for no reason')
if st.button('About'):
    st.text('Welcome to Arions Troops Streamlit App')

name = st.text_input('Enter your name', 'Type Here ...')
if st.button('Submit'):
    result = name.title()
    st.success(result)
    
level = st.slider('Select the level', 1, 5)
st.text('Selected: {}'.format(level))


