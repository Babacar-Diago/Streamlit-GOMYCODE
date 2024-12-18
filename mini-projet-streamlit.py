# import the streamlit library
import streamlit as st

# give a title to our app
st.title('Welcome to BMI Calculator')

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)", min_value=0.0)

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))

bmi = 0

if status == 'cms':
    height = st.number_input('Centimeters', min_value=0.0)
    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text("Enter some value of height")
elif status == 'meters':
    # take height input in meters
    height = st.number_input('Meters', min_value=0.0)
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")
else:
    height = st.number_input('Feet', min_value=0.0)
    # 1 meter = 3.28 feet
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")

# vérifier si le bouton est pressé ou non :
if (st.button('Calculate BMI')):
    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))
    # give the interpretation of BMI index
    if bmi < 16:
        st.error("You are Extremely Underweight")

    # elif bmi >= 16 and bmi < 18.5:
    elif 16 <= bmi < 18.5:
        st.warning("You are Underweight")

    # elif bmi >= 18.5 and bmi < 25:
    elif 18.5 <= bmi < 25:
        st.success("Healthy")

    # elif bmi >= 25 and bmi < 30:
    elif 25 <= bmi < 30:
        st.warning("Overweight")

    elif bmi >= 30:
        st.error("Extremely Overweight")
