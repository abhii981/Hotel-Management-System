import streamlit as st
from db import get_connection

st.title("📊 Reports")

date = st.date_input("Select booking date for availability check")
hotel_id = st.number_input("Enter Hotel ID", min_value=1, step=1)

if st.button("Check Availability"):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        (SELECT hotel_room_capacity 
         FROM hotel 
         WHERE hotel_id = %s) AS Total_Rooms,

        (SELECT IFNULL(SUM(total_rooms_booked), 0)
         FROM bookings 
         WHERE hotel_hotel_id = %s
           AND DATE(booking_date) = %s) AS Total_Rooms_Booked,

          FROM hotel 
          WHERE hotel_id = %s)
         -
         (SELECT IFNULL(SUM(total_rooms_booked), 0)
          FROM bookings 
          WHERE hotel_hotel_id = %s
            AND DATE(booking_date) = %s)
        ) AS Available_Rooms
    """

    cursor.execute(query, (hotel_id, hotel_id, date, hotel_id, hotel_id, date))
    result = cursor.fetchone()

    st.write("### 📌 Room Availability Summary")
    st.write(result)
