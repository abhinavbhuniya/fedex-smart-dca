import streamlit as st
from ml_model import predict_case

st.set_page_config(page_title="FedEx Smart DCA Control Tower")

st.title("FedEx Smart DCA Control Tower")

st.subheader("Case Priority Predictor")

amount = st.number_input("Overdue Amount (₹)", min_value=1000)
days = st.number_input("Days Overdue", min_value=1)
past = st.selectbox("Past Recovery Success", [0, 1])
risk = st.selectbox("Customer Risk Level (1=Low, 3=High)", [1, 2, 3])

if st.button("Predict Priority"):
    prob, priority = predict_case([amount, days, past, risk])
    st.success(f"Recovery Probability: {prob:.2f}")
    st.warning(f"Priority Level: {priority}")
