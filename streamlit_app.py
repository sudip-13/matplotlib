import streamlit as st
import time as t
# Title
st.title("Welcome to Room")
#adding image
st.image("ro.jpg")
#Heading
st.header("Machine Learning")
#subheader
st.subheader("Linear Regression")
#To give information
st.info("Information details of user")
#To give warning
st.warning("Come in time else you will be marked as absent")
#Error message
st.error("Wrong Password")
#Success message
st.success("Congarts you get pp in sem-4")
# write
st.write("Enter employee name")
st.write(range(50))
#Markdown
st.markdown("# Intellipat")
st.markdown("## Intellipat")
st.markdown("### Intellipat")
st.markdown(":moon:")
#text
st.text("Intellipaat Learners")
#caption
st.caption("Caption is here")
# representation of mathematical equation
st.latex('''ax^2+bx+c''')
#widget
#checkbox
st.checkbox("Log in")
#button
st.button("Submit")
# radio widget
st.radio("Select your gender",["Male","Female","Others"])
#select box
st.selectbox("Pick your course",["ML","Cloud","Cyber Security"])
#multiselect
st.multiselect("choose department",["Content","Sales","Marketing"])
#selectslider
st.select_slider("Rating",["Bad","Good","Excellent","Outstanding"])
#slider
st.slider("Enter Your number",0,30)
#number_input
st.number_input("Pick your number",0,100)
#text_input
st.text_input("Enter your email address")
#date input
st.date_input("Opening Ceremony")
#time input
st.time_input("Hey! what's the timing")
# text area 
st.text_area("Welcome to Room to fell chill")
#file upload
st.file_uploader("Enter your pic")
#color_picker
st.color_picker("Select any color")
#progessor
st.progress(90)
#spinner
with st.spinner("Just Wait"):
    t.sleep(2)
#ballons
st.balloons()
#sidebar
st.sidebar.title("Welcome to intellipaat")
st.sidebar.text_input("Enter Your Mail Adress")
st.sidebar.text_input("Password")
st.sidebar.button("Click")
st.sidebar.radio("Professional Experts",["Student","Working professional","Others"])
#Data visulization
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
st.title("Bar Chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["X","Y"])
st.bar_chart(data)
# data1 = {'C':20, 'C++':15, 'Java':30,
#         'Python':35}
# courses = list(data1.keys())
# values = list(data1.values())
# plt.bar(courses,values)
st.title("Line Chart")
st.line_chart(data)
st.title("Area Chart")
st.area_chart(data)