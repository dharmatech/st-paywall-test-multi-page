
import urllib.parse
import streamlit as st
import stripe
import st_paywall
import urllib

def is_email_subscribed_to_product(email, product):
    for customer in stripe.Customer.list(email=email):
        for subscription in stripe.Subscription.list(customer=customer['id']):
            if subscription['plan']['product'] == product:
                return True
    return False

def product_auth(redirect_url, product, payment_link):

    email = st_paywall.google_auth.get_logged_in_user_email()

    st_paywall.google_auth.redirect_url = redirect_url

    if not email:
        st_paywall.google_auth.show_login_button(text='Login with Google', sidebar=True)
        st.stop()

    stripe.api_key = st_paywall.stripe_auth.get_api_key()

    is_subscribed = is_email_subscribed_to_product(email, product)

    if not is_subscribed:

        if st.sidebar.button(label='logout', type='primary'):
            del st.session_state.email
            st.rerun()

        encoded_email = urllib.parse.quote(email)

        url = payment_link

        url = f'{url}?prefilled_email={encoded_email}'

        st.sidebar.link_button(label='subscribe', url=url)
        st.stop()

    if st.sidebar.button(label='logout', type='primary'):
        del st.session_state.email
        st.rerun()


