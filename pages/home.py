# filepath: /pages/home.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.supabase_client import supabase

st.title('Exercise Tracker')

# Example: Fetch data from Supabase
exercises = supabase.table('exercises').select('*').execute()
st.write(exercises.data)