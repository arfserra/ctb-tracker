# filepath: /streamlit_app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'pages')))

import streamlit as st
from pages import add_exercise
from pages import view_exercises
from pages import log_workout
from utils.supabase_client import supabase
from datetime import datetime

# Function to fetch the last 5 workouts
def fetch_last_workouts():
    try:
        # Fetch the last 5 workouts
        workout_logs_response = supabase.table('workout_logs').select('*').order('logged_at', desc=True).limit(5).execute()
        workout_logs = workout_logs_response.data

        if not workout_logs:
            return []

        workouts = []
        for log in workout_logs:
            workout_id = log['id']
            day = datetime.fromisoformat(log['logged_at']).strftime('%A, %B %d, %Y')

            # Fetch exercises for the workout
            exercises_response = supabase.table('workout_exercises').select('*').eq('workout_id', workout_id).execute()
            exercises = exercises_response.data

            workout_details = {'day': day, 'exercises': []}
            for exercise in exercises:
                exercise_id = exercise['exercise_id']
                weight_kg = exercise['weight']
                weight_lb = weight_kg * 2.20462

                # Fetch series for the exercise
                series_response = supabase.table('series').select('*').eq('workout_exercise_id', exercise['id']).execute()
                series = series_response.data

                series_details = [f"S{idx+1}x{serie['repetition_count']}" for idx, serie in enumerate(series)]

                # Fetch the exercise name and day from the exercises table
                exercise_name_response = supabase.table('exercises').select('name, day').eq('id', exercise_id).execute()
                exercise_data = exercise_name_response.data[0] if exercise_name_response.data else {'name': 'Unknown', 'day': 'None'}

                workout_details['exercises'].append({
                    'name': exercise_data['name'],
                    'day': exercise_data['day'],
                    'series': ', '.join(series_details),
                    'weight_kg': round(weight_kg, 2),
                    'weight_lb': round(weight_lb, 2)
                })

            workouts.append(workout_details)

        return workouts
    except Exception as e:
        st.error(f"An error occurred while fetching workouts: {str(e)}")
        return []

# Get the current page from query params
page = st.query_params.get('page', ['home'])[0]

if page == 'home':
    st.title('Exercise Tracker')

        # Buttons to navigate to other pages, side by side
    col1, col2 = st.columns(2)
    with col1:
            if st.button('Log Workout', type="primary", use_container_width=True):
                st.query_params = {'page': 'log_workout'}
    with col2:
            if st.button('View Exercises', type="secondary", use_container_width=True):
                st.query_params = {'page': 'view_exercises'}

    # Display the last 5 workouts
    st.subheader('Last 5 Workouts')
    workouts = fetch_last_workouts()
    if workouts:
        for workout in workouts:
            st.markdown(f"<span style='color: #ebbe4d; font-weight: bold;'>{workout['day']}</span>", unsafe_allow_html=True)
            for exercise in workout['exercises']:
                st.write(f"- {exercise['day']}*{exercise['name']}, **Series:** {exercise['series']}, **Max:** {exercise['weight_kg']} kg / {exercise['weight_lb']} lb")
            st.write("---")
    else:
        st.write("No workouts found.")

elif page == 'add_exercise':
    add_exercise.main()
elif page == 'view_exercises':
    view_exercises.main()
elif page == 'log_workout':
    log_workout.main()