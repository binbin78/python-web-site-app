import streamlit as st
import pandas

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

data = pandas.read_csv("data.csv", sep=";")

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row["image"]}")
        st.markdown(f"[Source Code]({row["url"]})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.markdown(f"[Source Code]({row["url"]})")