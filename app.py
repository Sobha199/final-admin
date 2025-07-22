
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
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")
st.title("📊 Dashboard")

# Load CSV
df = pd.read_csv("Tracking.csv")

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# Check for 'emp status' column
if "emp status" in df.columns:
    active_count = df[df["emp status"].str.lower() == "active"].shape[0]
    inactive_count = df[df["emp status"].str.lower() != "active"].shape[0]

    st.metric("Active Employees", active_count)
    st.metric("Inactive Employees", inactive_count)
else:
    st.error("'Emp Status' column not found in the uploaded data.")
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Overview", page_icon="🧾", layout="wide")
st.title("🧾 Overview")

# Load and clean CSV
df = pd.read_csv("Tracking.csv")

# Remove duplicate columns
df = df.loc[:, ~df.columns.duplicated()]

# Display dataframe
st.dataframe(df)

# Option to download Excel
excel = df.to_excel(index=False, engine='openpyxl')
st.download_button("Download Excel", data=excel, file_name="overview_data.xlsx")


