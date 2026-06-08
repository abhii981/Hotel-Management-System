import streamlit as st
import mysql.connector

st.title("➕ Add New Guest")

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="abhi",   
        database="hotel_database"
    )

guest_id = st.number_input("Guest ID (must be unique)", min_value=1, step=1)
fname = st.text_input("First Name")
lname = st.text_input("Last Name")
contact = st.text_input("Contact Number")
email = st.text_input("Email Address")
address_id = st.number_input("Address ID (must exist in addresses table)", min_value=1, step=1)

if st.button("Add Guest"):
    if not fname or not lname or not contact or not email:
        st.error("Please fill all fields.")
    else:
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO guests
                (guest_id, guest_first_name, guest_last_name, guest_contact_number,
                 guest_email_address, guest_credit_card, guest_id_proof, addresses_address_id)
                VALUES (%s, %s, %s, %s, %s, NULL, NULL, %s)
            """

            cursor.execute(query, (guest_id, fname, lname, contact, email, address_id))
            conn.commit()

            st.success(f"Guest '{fname} {lname}' added successfully!")

        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
