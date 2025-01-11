import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.supabase_client import supabase

def main():
    # Button to navigate back to home page
    if st.button('Back to Home'):
        st.query_params(page='home')

    st.title('Add Exercise')

    # Initialize session state keys
    if 'name' not in st.session_state:
        st.session_state['name'] = ''
    if 'type' not in st.session_state:
        st.session_state['type'] = ''
    if 'description' not in st.session_state:
        st.session_state['description'] = ''
    if 'day' not in st.session_state:
        st.session_state['day'] = 'A'



    # Input fields
    name = st.text_input('Name', max_chars=100, value=st.session_state['name'])
    type = st.selectbox('Type', ['Strength', 'Cardio', 'Mobility'], index=0 if st.session_state['type'] == '' else ['Strength', 'Cardio', 'Mobility'].index(st.session_state['type']))
    description = st.text_area('Description', value=st.session_state['description'])
    day = st.radio('Day', ['A', 'B', 'Rest'], index=['A', 'B', 'Rest'].index(st.session_state['day']))

    if st.button('Add Exercise'):
        if not name or not type or not day:
            st.error('Name, type, and day are required.')
        else:
            try:
                # Insert exercise data
                data = {
                    'name': name,
                    'type': type,
                    'description': description,
                    'day': day
                }
                
                response = supabase.table('exercises').insert(data).execute()
                
                # Handle success
                st.success('Exercise added successfully!')

            except Exception as e:
                st.error(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    main()