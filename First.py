import streamlit as st
st.title('Welcome to Arion Troop BMI Calclator App')
st.subheader('Calculate your Body Mass Index (BMI) easily!')

weight = st.number_input('Enter your weight (in kgs)')

status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))

if status == 'cms':
    height = st.number_input('Centimeters')
    
    try:
        bmi = weight/((height/100)**2)
    except:
        st.text('Enter some value of height')

if status == 'meters':
    height = st.number_input('Meters')
    
    try:
        bmi = weight/(height**2)
    except:
        st.text('Enter some value of height')

if status == 'feet':
    height = st.number_input('Feet')
    
    try:
        bmi = weight/(((height*0.3048))**2)
    except:
        st.text('Enter some value of height')

if(st.button('Calculate BMI')):
    st.text('Your BMI Index is {}.'.format(bmi))

    if(bmi < 16):
        st.error('You are extremely underweight')
    elif(bmi >= 16 and bmi < 18.5):
        st.warning('You are underweight')
    elif(bmi >= 10.5 and bmi < 25):
        st.success("healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning('Overweight')
    elif(bmi >= 30 ):
        st.error('Extremely Overweight')