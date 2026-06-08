import streamlit as st
import mysql.connector
from datetime import date

st.title("🛌 Add New Booking")

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="abhi",   
        database="hotel_database"
    )

def fetch_data(query):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

guests = fetch_data("SELECT guest_id, guest_first_name FROM guests")
employees = fetch_data("SELECT emp_id, emp_first_name FROM employees")
hotels = fetch_data("SELECT hotel_id, hotel_name FROM hotel")

booking_id = st.number_input("Booking ID (must be unique)", min_value=1, step=1)

guest_choice = st.selectbox(
    "Select Guest",
    options=guests,
    format_func=lambda x: f"{x['guest_id']} - {x['guest_first_name']}"
)

employee_choice = st.selectbox(
    "Select Employee",
    options=employees,
    format_func=lambda x: f"{x['emp_id']} - {x['emp_first_name']}"
)

hotel_choice = st.selectbox(
    "Select Hotel",
    options=hotels,
    format_func=lambda x: f"{x['hotel_id']} - {x['hotel_name']}"
)

booking_date = st.date_input("Booking Date", date.today())
check_in = st.date_input("Check-in Date", date.today())
check_out = st.date_input("Check-out Date", date.today())
duration = st.number_input("Duration of Stay (in days)", min_value=1)
rooms_booked = st.number_input("Total Rooms Booked", min_value=1)
payment = st.selectbox("Payment Type", ["cash", "card"])
amount = st.number_input("Total Amount", min_value=0)

if st.button("Add Booking"):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO bookings
            (booking_id, booking_date, duration_of_stay, check_in_date, check_out_date,
             booking_payment_type, total_rooms_booked, hotel_hotel_id,
             guests_guest_id, employees_emp_id, total_amount)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            booking_id,
            booking_date,
            duration,
            check_in,
            check_out,
            payment,
            rooms_booked,
            hotel_choice["hotel_id"],
            guest_choice["guest_id"],
            employee_choice["emp_id"],
            amount
        ))

        conn.commit()
        st.success(f"Booking {booking_id} added successfully!")

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
