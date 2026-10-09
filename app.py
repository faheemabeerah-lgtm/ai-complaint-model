
%%writefile app.py
import streamlit as st

st.set_page_config(
    page_title="AI Complaint Resolution Agent",
    page_icon="🎧",
    layout="wide"
)

st.title("AI Complaint Resolution Agent")
st.write(
    "Submit a customer complaint to receive an AI-generated "
    "analysis and a recommended resolution."
)

st.info(
    "This interface is a prototype. The next step will connect "
    "the form to your Groq-powered workflow."
)

with st.form("complaint_form"):
    customer_name = st.text_input("Customer name (optional)")
    order_id = st.text_input("Order ID (optional)")
    complaint = st.text_area(
        "Describe your complaint",
        placeholder="Explain what happened...",
        height=150
    )

    submitted = st.form_submit_button("Analyze Complaint")

if submitted:
    if not complaint.strip():
        st.error("Please enter your complaint first.")
    else:
        st.subheader("Complaint Received")
        st.write("**Customer:**", customer_name or "Not provided")
        st.write("**Order ID:**", order_id or "Not provided")
        st.write("**Complaint:**")
        st.write(complaint)

        st.success(
            "Your complaint has been received. "
            "AI analysis will be connected in the next step."
        )
