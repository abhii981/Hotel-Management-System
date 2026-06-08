import streamlit as st
from db import get_connection

st.title("🗑 Delete Booking")

conn = get_connection()
cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT booking_id FROM bookings")
bookings = cursor.fetchall()

booking = st.selectbox("Select Booking ID to Delete", bookings, format_func=lambda x: f"{x['booking_id']}")

if st.button("Delete Booking"):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bookings WHERE booking_id = %s", (booking["booking_id"],))
    conn.commit()

    st.success("Booking deleted successfully! (Audit trigger executed automatically)")
