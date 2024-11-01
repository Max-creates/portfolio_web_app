import streamlit as st
import pandas as pd

st.header("My Certificates")

content = """

Below you can find all of my certificates and links.

"""

st.subheader(content)

col5, empty_col = st.columns(2)

df_certificates = pd.read_csv("certificates.csv", sep=";")

with col5:
    for index, row in df_certificates.iterrows():

        st.image("certificates/" + row["image"])
        st.write(row["description"])
        st.write(f"[Link]({row['url']})")
        st.divider()