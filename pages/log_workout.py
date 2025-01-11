import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.supabase_client import supabase

def main():
    st.title('Log Workout')

    # Fetch exercises from Supabase
    try:
        response = supabase.table('exercises').select('*').execute()
        exercises = response.data
        if exercises is None:
            st.error("Error fetching exercises.")
            return
        elif not exercises:
            st.info("No exercises found.")
            return
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return

    # Select day
    day = st.radio('Select Day', ['A', 'B', 'Rest'])

    # Initialize session state for workout
    if 'workout' not in st.session_state:
        st.session_state['workout'] = []

    # Filter exercises by selected day
    filtered_exercises = [exercise for exercise in exercises if exercise.get('day') == day]

    # Select exercise
    exercise_names = [exercise['name'] for exercise in filtered_exercises]
    selected_exercise = st.radio('Select Exercise', exercise_names)

    # Display selected exercise details
    if selected_exercise:
        selected_exercise_data = next((exercise for exercise in filtered_exercises if exercise['name'] == selected_exercise), None)
        if selected_exercise_data:
            st.image(selected_exercise_data.get('image_url', 'https://via.placeholder.com/150'), width=150)
            st.write(f"Description: {selected_exercise_data.get('description', 'No Description')}")

    # Input fields
    series = st.number_input('Series', min_value=1, step=1)
    repetitions = st.number_input('Repetitions', min_value=1, step=1)
    weight = st.number_input('Weight (kg)', min_value=0.0, step=0.1)
    notes = st.text_area('Notes')

    if st.button('Add Exercise to Workout'):
        if not selected_exercise or series <= 0 or repetitions <= 0 or weight < 0:
            st.error('Please fill in all fields correctly.')
        else:
            # Add exercise to workout
            st.session_state['workout'].append({
                'exercise': selected_exercise,
                'series': series,
                'repetitions': repetitions,
                'weight': weight,
                'notes': notes
            })
            st.success('Exercise added to workout!')

    # Display current workout
    st.subheader('Current Workout')
    for i, exercise in enumerate(st.session_state['workout']):
        st.write(f"{i+1}. {exercise['exercise']} - Series: {exercise['series']}, Repetitions: {exercise['repetitions']}, Weight: {exercise['weight']} kg, Notes: {exercise['notes']}")

    if st.button('Log Workout'):
        if not st.session_state['workout']:
            st.error('Please add at least one exercise to the workout.')
        else:
            try:
                # Insert workout log data
                data = {
                    'day': day,
                    'exercises': st.session_state['workout']
                }
                
                response = supabase.table('workout_logs').insert(data).execute()
                
                # Handle success
                st.success('Workout logged successfully!')
                # Clear workout
                st.session_state['workout'] = []
                st.experimental_rerun()

            except Exception as e:
                st.error(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    main()