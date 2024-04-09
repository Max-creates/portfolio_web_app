import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")
    
with col2:
    st.title("Maksym Solomyanov")
    content = """
    Hi, I am Maksym. I am a Python programmer.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[11:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        
with col4:
    for index, row in df[:11].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        
content3 = """

Below you can find all of my certificates and links.

"""

st.header(content3)

col5, empty_col = st.columns(2)

df_certificates = pd.read_csv("certificates.csv", sep=";")

with col5:
    for index, row in df_certificates.iterrows():

        st.image("certificates/" + row["image"])
        st.write(row["description"])
        st.write(f"[Link]({row['url']})")

        