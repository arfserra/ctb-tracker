# filepath: /streamlit_app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'pages')))

import streamlit as st
from pages import add_exercise
from pages import view_exercises
from pages import log_workout

# Get the current page from query params
page = st.query_params.get('page', ['home'])[0]

if page == 'home':
    st.title('Exercise Tracker')

    # Button to navigate to add_exercise page
    if st.button('Add Exercise'):
        st.query_params = {'page': 'add_exercise'}

    # Button to navigate to view_exercises page
    if st.button('View Exercises'):
        st.query_params = {'page': 'view_exercises'}

    # Button to navigate to log_workout page
    if st.button('Log Workout'):
        st.query_params = {'page': 'log_workout'}

elif page == 'add_exercise':
    add_exercise.main()
elif page == 'view_exercises':
    view_exercises.main()
elif page == 'log_workout':
    log_workout.main()