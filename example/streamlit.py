import streamlit as st
import pandas as pd

st.write(""" Hello World""")

df = pd.read_csv('data.csv')
st.line_chart(df['synopsis'])