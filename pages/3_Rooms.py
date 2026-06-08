import streamlit as st
import pandas as pd
from db import get_connection

st.title("🛏 Rooms")

conn = get_connection()
cursor = conn.cursor(dictionary=True)

query = """
SELECT
    r.room_id,
    r.room_number,

    (SELECT room_type_name
     FROM room_type
     WHERE room_type_id = r.rooms_type_rooms_type_id) AS room_type,

    (SELECT hotel_name
     FROM hotel
     WHERE hotel_id = r.hotel_hotel_id) AS hotel_name

FROM rooms r;
"""

cursor.execute(query)
rows = cursor.fetchall()

df = pd.DataFrame(rows)
st.dataframe(df)
