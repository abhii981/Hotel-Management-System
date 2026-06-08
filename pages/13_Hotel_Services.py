import streamlit as st
import mysql.connector

st.title("🛎️ Hotel Services Management")

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="abhi",    
        database="hotel_database"
    )

def fetch_hotels():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT hotel_id, hotel_name FROM hotel")
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_bookings():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT booking_id FROM bookings")
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_services():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT service_id, service_name, service_cost, hotel_hotel_id FROM hotel_services"
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

st.subheader("➕ Add Service to a Hotel")

hotels = fetch_hotels()
hotel_list = {f"{h['hotel_id']} - {h['hotel_name']}": h['hotel_id'] for h in hotels}

hotel_choice = st.selectbox("Select Hotel", list(hotel_list.keys()))

service_name = st.text_input("Service Name")
service_description = st.text_input("Service Description")
service_cost = st.number_input("Service Cost", min_value=0, step=50)

if st.button("Add Service"):
    if not service_name:
        st.error("Service name cannot be empty!")
    else:
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO hotel_services 
                (service_name, service_description, service_cost, hotel_hotel_id)
                VALUES (%s, %s, %s, %s)
            """

            cursor.execute(query, (
                service_name,
                service_description,
                service_cost,
                hotel_list[hotel_choice]
            ))
            conn.commit()

            st.success("Service added successfully!")

        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

        finally:
            conn.close()


st.subheader("📋 View All Hotel Services")

services = fetch_services()

for svc in services:
    st.write(
        f"**Service ID:** {svc['service_id']}  |  "
        f"**Name:** {svc['service_name']}  |  "
        f"**Cost:** ₹{svc['service_cost']}  |  "
        f"**Hotel ID:** {svc['hotel_hotel_id']}"
    )

st.subheader("🧾 Assign Service to a Booking")

bookings = fetch_bookings()
booking_list = [str(b["booking_id"]) for b in bookings]

services_dict = {f"{s['service_id']} - {s['service_name']}": s["service_id"] for s in services}

selected_booking = st.selectbox("Select Booking ID", booking_list)
selected_service = st.selectbox("Select Service", list(services_dict.keys()))

if st.button("Assign Service"):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO hotel_services_used_by_guests
            (hotel_services_service_id, bookings_booking_id)
            VALUES (%s, %s)
        """

        cursor.execute(query, (
            services_dict[selected_service],
            selected_booking
        ))
        conn.commit()

        st.success("Service assigned to booking!")

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

    finally:
        conn.close()
