import streamlit as st
from send_email import send_email

st.set_page_config(layout="wide")

st.header("Contact Us")

with st.form(key="contact_form"):
    user_email=st.text_input("Your email address")
    message_box = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{message_box}
"""
    button = st.form_submit_button("Submit") 

    if button:
       
        send_email(message)

        st.info("Your email was sent successfully!")
