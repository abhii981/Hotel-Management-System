import streamlit as st
import pandas as pd
from db import get_connection

st.title("💰 Revenue Report")

conn = get_connection()
cursor = conn.cursor(dictionary=True)

option = st.selectbox("Select Revenue Type", ["Monthly Revenue", "Total Revenue"])

if option == "Monthly Revenue":
    month = st.number_input("Enter Month (1–12)", min_value=1, max_value=12)
    year = st.number_input("Enter Year", min_value=2000, max_value=2100)

    if st.button("Get Monthly Revenue"):
        query = """
        SELECT SUM(total_amount) AS revenue
        FROM bookings
        WHERE MONTH(booking_date) = %s AND YEAR(booking_date) = %s
        """
        cursor.execute(query, (month, year))
        result = cursor.fetchone()

        st.write("### Revenue:", result["revenue"])

else:
    if st.button("Get Total Revenue"):
        query = "SELECT SUM(total_amount) AS revenue FROM bookings"
        cursor.execute(query)
        result = cursor.fetchone()

        st.write("### Total Revenue:", result["revenue"])
