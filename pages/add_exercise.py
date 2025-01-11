# filepath: /pages/add_exercise.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.supabase_client import supabase
from PIL import Image
import io

st.title('Add Exercise')

# Input fields
name = st.text_input('Name', max_chars=100)
type = st.selectbox('Type', ['Strength', 'Cardio', 'Mobility'])
description = st.text_area('Description')
image = st.file_uploader('Upload Image', type=['jpg', 'jpeg', 'png'])

if st.button('Add Exercise'):
    if not name or not type:
        st.error('Name and type are required.')
    elif image and image.size > 2 * 1024 * 1024:
        st.error('Image size should be under 2 MB.')
    else:
        image_url = ''
        if image:
            image_bytes = image.read()
            image_name = image.name
            image_path = f'exercise-images/{image_name}'
            data, error = supabase.storage().from_('exercise-images').upload(image_path, image_bytes)
            if error:
                st.error('Error uploading image.')
            else:
                image_url = supabase.storage().from_('exercise-images').get_public_url(image_path)

        data, error = supabase.from_('exercises').insert([
            { 'name': name, 'type': type, 'description': description, 'image_url': image_url }
        ]).execute()

        if error:
            st.error('Error saving exercise.')
        else:
            st.success('Exercise added successfully!')
            # Clear inputs
            name = ''
            type = ''
            description = ''
            image = None