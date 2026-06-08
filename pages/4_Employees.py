import streamlit as st
import pandas as pd
from db import get_connection

st.title("👨‍💼 Employees")

conn = get_connection()
cursor = conn.cursor(dictionary=True)

query = """
SELECT
    e.emp_id,
    e.emp_first_name,
    e.emp_last_name,
    e.emp_designation,

    (SELECT department_name
     FROM department
     WHERE department_id = e.department_department_id) AS department_name,

    (SELECT hotel_name
     FROM hotel
     WHERE hotel_id = e.hotel_hotel_id) AS hotel_name

FROM employees e;
"""

cursor.execute(query)
rows = cursor.fetchall()

df = pd.DataFrame(rows)
st.dataframe(df)
