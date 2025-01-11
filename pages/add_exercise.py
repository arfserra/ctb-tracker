import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.supabase_client import supabase
import io

def main():
    # Button to navigate back to home page
    if st.button('Back to Home'):
        st.query_params(page='home')

    st.title('Add Exercise')



    # Input fields
    name = st.text_input('Name', max_chars=100)
    type = st.selectbox('Type', ['Strength', 'Cardio', 'Mobility'])
    description = st.text_area('Description')

    if st.button('Add Exercise'):
        if not name or not type:
            st.error('Name and type are required.')
        else:
            try:
                # Insert exercise data
                data = {
                    'name': name,
                    'type': type,
                    'description': description
                }
                
                response = supabase.table('exercises').insert(data).execute()
                
                # Handle success
                st.success('Exercise added successfully!')
                # Clear form using session state
                st.session_state.name = ''
                st.session_state.description = ''

            except Exception as e:
                st.error(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    main()