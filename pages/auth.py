import streamlit as st
from utils.supabase_client import supabase
from gotrue.errors import AuthApiError

def sign_up(email, password):
    response = supabase.auth.sign_up({
        'email': email,
        'password': password,
        'options': {
            'email_redirect_to': 'https://your-redirect-url.com/welcome'
        }
    })
    return response

def sign_in_with_password(email, password):
    response = supabase.auth.sign_in_with_password({
        'email': email,
        'password': password
    })
    return response

def main():
    st.title('CTB Tracker')

    # Tabs for login and sign-up
    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        st.header("Login")
        email = st.text_input('Email', key='login_email')
        password = st.text_input('Password', type='password', key='login_password')
        if st.button('Login'):
            if email and password:
                try:
                    response = sign_in_with_password(email, password)
                    st.success('Logged in successfully!')
                    st.session_state['user'] = response.user
                    st.session_state['access_token'] = response.session.access_token
                    st.query_params['page'] = 'home'
                    st.rerun()
                except AuthApiError as e:
                    st.error(f"Login failed: {e}")
            else:
                st.error('Please provide both email and password.')

    with tab2:
        st.header("Sign Up")
        email = st.text_input('Email', key='signup_email')
        password = st.text_input('Password', type='password', key='signup_password')
        if st.button('Sign Up'):
            if email and password:
                try:
                    response = sign_up(email, password)
                    st.success('Signed up successfully! Please check your email to confirm your account.')
                    st.query_params['page'] = 'home'
                    st.rerun()
                except AuthApiError as e:
                    st.error(f"Sign up failed: {e}")
            else:
                st.error('Please provide both email and password.')

if __name__ == "__main__":
    main()