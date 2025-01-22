import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.supabase_client import supabase

def main():
    st.title('Log Workout')

    # Check if user is logged in
    if 'user' not in st.session_state:
        st.warning('Please log in to access this page.')
        st.query_params['page'] = 'auth'
        st.rerun()
        return

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

    # Initialize session state for workout
    if 'workout' not in st.session_state:
        st.session_state['workout'] = {'exercises': []}

    # Initialize session state for weight conversion
    if 'weight_kg' not in st.session_state:
        st.session_state['weight_kg'] = 0.0
    if 'weight_lb' not in st.session_state:
        st.session_state['weight_lb'] = 0.0

    # Callback functions for weight conversion
    def kg_to_lb():
        st.session_state.weight_lb = st.session_state.weight_kg * 2.20462

    def lb_to_kg():
        st.session_state.weight_kg = st.session_state.weight_lb / 2.20462

    # Select day
    day = st.radio('Select Day', ['A', 'B', 'Rest'], horizontal=True)

    # Filter exercises by selected day
    filtered_exercises = [exercise for exercise in exercises if exercise.get('day') == day]

    # Select exercise
    exercise_names = [exercise['name'] for exercise in filtered_exercises]
    selected_exercise = st.selectbox('Select Exercise', exercise_names)

    # Display selected exercise details
    if selected_exercise:
        selected_exercise_data = next((exercise for exercise in filtered_exercises if exercise['name'] == selected_exercise), None)
        if selected_exercise_data:
            st.image(selected_exercise_data.get('image_url', 'https://via.placeholder.com/150'), width=150)
            st.write(f"Description: {selected_exercise_data.get('description', 'No Description')}")

    # Input fields for weight and series
    col1, col2 = st.columns(2)
    with col1:
        st.number_input('Weight (kg)', min_value=0.0, step=2.26796, key='weight_kg', on_change=kg_to_lb)  # 5 lb in kg
    with col2:
        st.number_input('Weight (lb)', min_value=0.0, step=5.0, key='weight_lb', on_change=lb_to_kg)
    
    repetitions = st.number_input('Repetitions', min_value=1, step=1)

    if st.button('Add Series'):
        if not selected_exercise or repetitions <= 0 or st.session_state['weight_kg'] < 0:
            st.error('Please fill in all fields correctly.')
        else:
            # Add series to the selected exercise
            exercise_entry = next((exercise for exercise in st.session_state['workout']['exercises'] if exercise['name'] == selected_exercise), None)
            if not exercise_entry:
                exercise_entry = {'name': selected_exercise, 'weight': st.session_state['weight_kg'], 'series': []}
                st.session_state['workout']['exercises'].append(exercise_entry)
            exercise_entry['series'].append({'repetitions': repetitions})
            st.success('Series added to exercise!')

    # Display current workout
    st.subheader('Current Workout')
    for i, exercise in enumerate(st.session_state['workout']['exercises']):
        weight_kg = exercise['weight']
        weight_lb = weight_kg * 2.20462
        st.write(f"{i+1}. {exercise['name']} - Weight: {weight_kg:.2f} kg / {weight_lb:.2f} lb")
        for j, serie in enumerate(exercise['series']):
            st.write(f"  Series {j+1}: {serie['repetitions']} repetitions")

    if st.button('Add Another Exercise'):
        st.query_params = {'page': 'log_workout'}

    if st.button('Log Workout'):
        if not st.session_state['workout']['exercises']:
            st.error('Please add at least one exercise to the workout.')
        else:
            try:
                # Insert workout log data
                workout_response = supabase.table('workout_logs').insert({}).execute()
                if workout_response.data is None:
                    st.error(f"Error inserting workout: {workout_response}")
                    return
                workout_id = workout_response.data[0]['id']

                # Insert exercises and series data
                for exercise in st.session_state['workout']['exercises']:
                    exercise_data = {
                        'workout_id': workout_id,
                        'exercise_id': next(ex for ex in exercises if ex['name'] == exercise['name'])['id'],
                        'weight': exercise['weight'],
                        'notes': ''
                    }
                    exercise_response = supabase.table('workout_exercises').insert(exercise_data).execute()
                    if exercise_response.data is None:
                        st.error(f"Error inserting exercise: {exercise_response}")
                        return
                    workout_exercise_id = exercise_response.data[0]['id']

                    for serie in exercise['series']:
                        series_data = {
                            'workout_exercise_id': workout_exercise_id,
                            'repetition_count': serie['repetitions']
                        }
                        series_response = supabase.table('series').insert(series_data).execute()
                        if series_response.data is None:
                            st.error(f"Error inserting series: {series_response}")
                            return
                
                # Handle success
                st.success('Workout logged successfully!')
                # Clear workout
                st.session_state['workout'] = {'exercises': []}
                st.query_params = {'page': 'home'}

            except Exception as e:
                st.error(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    main()