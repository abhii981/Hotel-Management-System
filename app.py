import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Hotel Management System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg, #f0f4ff, #f9f9f9);
}

/* Header */
.header {
    background: linear-gradient(90deg, #1e3c72, #2a5298);
    padding: 35px;
    border-radius: 18px;
    color: white;
    text-align: center;
    margin-bottom: 35px;
}
.header h1 {
    font-size: 48px;
    margin-bottom: 5px;
}
.header p {
    font-size: 18px;
    opacity: 0.9;
}

/* Stat Cards */
.stat-card {
    background: white;
    padding: 25px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
}
.stat-number {
    font-size: 36px;
    font-weight: 700;
    color: #2a5298;
}
.stat-label {
    font-size: 14px;
    color: #666;
}

/* Feature Cards */
.feature-card {
    background: rgba(255,255,255,0.95);
    padding: 28px;
    border-radius: 18px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.09);
    transition: all 0.25s ease;
    height: 100%;
}
.feature-card:hover {
    transform: translateY(-6px);
}
.feature-title {
    font-size: 22px;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 10px;
}
.feature-text {
    font-size: 15px;
    color: #555;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 50px;
    font-size: 16px;
    color: #555;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("""
<div class="header">
    <h1>🏨 Hotel Management System</h1>
    <p>Smart database-driven hotel operations & analytics</p>
</div>
""", unsafe_allow_html=True)

# ---------------- Stats Section ----------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">120+</div>
        <div class="stat-label">Guests</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">85</div>
        <div class="stat-label">Bookings</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">15</div>
        <div class="stat-label">Services</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">₹2.4L</div>
        <div class="stat-label">Revenue</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- Features Section ----------------
f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">👤 Guest Management</div>
        <div class="feature-text">
            Maintain guest records, personal details, and address information
            with full database integrity and validation.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🛏 Booking Management</div>
        <div class="feature-text">
            Handle bookings, check-in/check-out dates, room allocation,
            and payment details efficiently.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🛎 Hotel Services</div>
        <div class="feature-text">
            Add hotel services like spa, laundry, gym and assign them
            to guest bookings dynamically.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

f4, f5, f6 = st.columns(3)

with f4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">👨‍💼 Employee Management</div>
        <div class="feature-text">
            Store employee details, departments, and hotel assignments
            using relational database design.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f5:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📊 Reports & Analytics</div>
        <div class="feature-text">
            Generate reports for bookings, revenue, room availability,
            and service usage using SQL queries.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f6:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🤖 Smart SQL Assistant</div>
        <div class="feature-text">
            Ask natural language questions and retrieve answers directly
            from the MySQL database.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown("""
<div class="footer">
Built with ❤️ by Abhi & Rudra
</div>
""", unsafe_allow_html=True)
