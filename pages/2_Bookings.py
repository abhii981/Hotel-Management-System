import streamlit as st
import pandas as pd
from db import get_connection

st.title("🛌 Bookings")

conn = get_connection()
cursor = conn.cursor(dictionary=True)

cursor.execute("""
SELECT 
 b.booking_id,
 g.guest_first_name,
 g.guest_last_name,
 b.booking_date,
 b.check_in_date,
 b.check_out_date,
 b.total_rooms_booked,
 h.hotel_name
FROM bookings b
JOIN guests g ON g.guest_id = b.guests_guest_id
JOIN hotel h ON h.hotel_id = b.hotel_hotel_id
""")

rows = cursor.fetchall()
df = pd.DataFrame(rows)
st.dataframe(df)
