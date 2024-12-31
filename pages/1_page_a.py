
import streamlit as st
import product_auth

product_auth.product_auth(
    redirect_url="http://localhost:8501/page_a", 
    product='prod_RUjARYvgx8U4NC',
    payment_link='https://buy.stripe.com/test_eVacPx4MD8cpfkYeV1')

st.write('page a')

