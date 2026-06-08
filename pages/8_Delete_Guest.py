import streamlit as st
from db import get_connection

st.title("🗑 Delete Guest")

conn = get_connection()
cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT guest_id, guest_first_name FROM guests")
guests = cursor.fetchall()

guest = st.selectbox("Select Guest to Delete", guests, format_func=lambda x: f"{x['guest_id']} - {x['guest_first_name']}")

if st.button("Delete Guest"):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM guests WHERE guest_id = %s", (guest["guest_id"],))
    conn.commit()
    st.success("Guest deleted successfully!")
