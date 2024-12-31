
import streamlit as st
import product_auth

product_auth.product_auth(
    redirect_url="http://localhost:8501/", 
    product='prod_RV6XoGskalCCyt',
    payment_link='https://buy.stripe.com/test_fZedTBa6X0JX6Os9AJ')

st.write('abc')

