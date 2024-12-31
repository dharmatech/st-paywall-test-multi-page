
import streamlit as st
import product_auth

product_auth.product_auth(
    redirect_url="http://localhost:8501/page_b", 
    product='prod_RV08XQZExyyKP9',
    payment_link='https://buy.stripe.com/test_00g02L4MD9gt2yc7sA')

st.write('page b')

