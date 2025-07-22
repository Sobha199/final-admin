
import streamlit as st

st.set_page_config(page_title="Admin Portal", page_icon=":bar_chart:", layout="wide")
st.markdown("<h1 style='text-align: center;'>Welcome to Admin Login</h1>", unsafe_allow_html=True)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "admin":
        st.success("Login successful! Please navigate to Dashboard or Overview using the sidebar.")
    else:
        st.error("Invalid username or password")
