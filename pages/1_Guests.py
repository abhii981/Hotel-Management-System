import streamlit as st
import pandas as pd
from db import get_connection

st.title("👤 Guests")

conn = get_connection()
cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT * FROM guests")
rows = cursor.fetchall()

df = pd.DataFrame(rows)
st.dataframe(df)
