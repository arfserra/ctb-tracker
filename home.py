# filepath: /streamlit_app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'pages')))

import streamlit as st
from pages import add_exercise

# Get the current page from query params
page = st.query_params().get('page', ['home'])[0]

if page == 'home':
    st.title('Exercise Tracker')

    # Button to navigate to add_exercise page
    if st.button('Add Exercise'):
        st.experimental_set_query_params(page='add_exercise')

    # Example: Fetch data from Supabase
    from utils.supabase_client import supabase
    exercises = supabase.table('exercises').select('*').execute()
    st.write(exercises.data)
elif page == 'add_exercise':
    add_exercise.main()