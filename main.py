import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/myphoto.jpg")
with col2:
    st.title("Binbin") 
    content=""" Hi, I am Binbin. I am learning the Python and use this application to do some practice."""  
    st.info(content) 

cotent2 = """Below you can find some of the apps I have build in Python. Feel free to contact me! """
st.write(cotent2)    