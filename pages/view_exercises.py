import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.supabase_client import supabase

def main():
    st.title('View Exercises')

    # Fetch data from Supabase
    try:
        response = supabase.table('exercises').select('*').execute()
        exercises = response.data
        if exercises is None:
            st.error("Error fetching data.")
        elif not exercises:
            st.info("No exercises found.")
        else:
            # Group exercises by day
            grouped_exercises = {'A': [], 'B': [], 'Rest': []}
            for exercise in exercises:
                day = exercise.get('day', 'No Day')
                if day in grouped_exercises:
                    grouped_exercises[day].append(exercise)
                else:
                    st.warning(f"Unexpected day value: {day}")

            # Sort exercises within each day in descending order by 'created_at'
            for day in grouped_exercises:
                grouped_exercises[day].sort(key=lambda x: x.get('created_at', ''), reverse=False)

            # Display exercises grouped by day
            for day, exercises in grouped_exercises.items():
                st.header(f"Day {day}")
                if not exercises:
                    st.write("No exercises for this day.")
                else:
                    for exercise in exercises:
                        name = exercise.get('name', 'No Name')
                        type = exercise.get('type', 'No Type')
                        description = exercise.get('description', 'No Description')
                        image_url = exercise.get('image_url', 'https://via.placeholder.com/150')
                        if not image_url:
                            image_url = 'https://via.placeholder.com/150'
                        
                        # Create a card layout using HTML and CSS
                        st.markdown(f"""
                        <div style="border: 1px solid #ddd; border-radius: 10px; padding: 10px; margin: 10px 0;">
                            <img src="{image_url}" style="width: 100%; border-radius: 10px;">
                            <h3>{name}</h3>
                            <p><strong>Type:</strong> {type}</p>
                            <p><strong>Description:</strong> {description}</p>
                        </div>
                        """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()