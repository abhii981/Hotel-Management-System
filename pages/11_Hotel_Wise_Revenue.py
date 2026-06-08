import streamlit as st
import pandas as pd
from db import get_connection

st.title("🏨 Hotel-wise Revenue Report")

conn = get_connection()
cursor = conn.cursor(dictionary=True)

query = """
SELECT
    (SELECT hotel_name 
     FROM hotel 
     WHERE hotel_id = b.hotel_hotel_id) AS hotel_name,

    SUM(b.total_amount) AS total_revenue

FROM bookings b
GROUP BY b.hotel_hotel_id
HAVING total_revenue > 0
ORDER BY total_revenue DESC;
"""

cursor.execute(query)
df = pd.DataFrame(cursor.fetchall())

st.dataframe(df)
