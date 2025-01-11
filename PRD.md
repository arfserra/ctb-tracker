# Product Requirements Document: Exercise Tracker Web App

## Foundation PRD

### Project Setup
**Objective:**  
Establish the foundational structure and tools for the exercise tracker web app using Streamlit for a simple, web-based interface.  

**Requirements:**  
- Use **Streamlit** for the UI framework to simplify development.  
- Include **Supabase** for cloud storage and authentication.  
- Use **Python** as the primary language for backend and logic.  
- Add **environment variables** for storing Supabase credentials securely.

**Deliverables:**  
1. A Streamlit app initialized with a basic structure.  
2. A Python script (`supabase_client.py`) to initialize and manage the Supabase client with the project's URL and anon key.  
3. A structured folder setup:
   - `/pages/` for Streamlit pages (e.g., Dashboard, AddExercise).
   - `/utils/` for utility/helper functions.
   - `/assets/` for static files if needed.

**Prompt for Copilot:**  
"Set up a Streamlit project for a web-based exercise tracker app. Create a Python file to initialize Supabase client using environment variables. Organize folders as `pages`, `utils`, and `assets` for scalability."

---

## Feature: Add Exercise

### Objective  
Allow users to create exercises with relevant details, including an optional image, and save them to the cloud.

### Requirements  
- **Input Fields:**  
  - Name (text input, required).  
  - Type (dropdown: Strength, Cardio, Mobility, required).  
  - Description (text area, optional).  
  - Image (file uploader, optional).  

- **Backend Integration:**  
  - Save exercise details to the `exercises` table in Supabase.  
  - Upload image to the Supabase storage bucket `exercise-images`.  
  - Store the image URL in the database.  

- **Validation:**  
  - Ensure all required fields are filled.  
  - Validate image size (<2 MB) and type (JPEG, PNG).

### Deliverables  
1. A Streamlit page (`add_exercise.py`) for adding exercises.  
2. Functionality to upload images to the storage bucket and link their URL to the exercise.  
3. Validation for required fields and image constraints.  

**Prompt for Copilot:**  
"Create a Streamlit page to add exercises. Include text inputs for name and description, a dropdown for type, and a file uploader for images. Use Python to validate inputs and save the data to Supabase's `exercises` table. Upload images to the `exercise-images` bucket and store the URL."

---

## Feature: View Exercises

### Objective  
Enable users to view all created exercises in a simple interface.

### Requirements  
- **UI Elements:**  
  - A list or grid showing the exercise name, type, description, and image.  

- **Backend Integration:**  
  - Fetch data from the `exercises` table in Supabase.  

### Deliverables  
1. A Streamlit page (`view_exercises.py`) for fetching and displaying exercise data.  
2. Exercises displayed in a card or table format showing the name, type, description, and image.  

**Prompt for Copilot:**  
"Create a Streamlit page to view exercises. Fetch data from the Supabase `exercises` table and display it in a table or card format with exercise name, type, description, and day."

---

## Feature: Log Workout

### Objective  
Allow users to log workout sessions by selecting an exercise and tracking repetitions, weights, and notes.

### Requirements  
- **Input Fields:**  
  - Dropdown to select an exercise (populated from the `exercises` table).  
  - Repetitions (number input, required).  
  - Weight (number input, required).  
  - Notes (text area, optional).  

- **Backend Integration:**  
  - Save workout logs to the `workout_logs` table in Supabase.  

- **Validation:**  
  - Ensure repetitions and weight are positive numbers.

### Deliverables  
1. A Streamlit page (`log_workout.py`) for logging workouts.  
2. Dropdown dynamically populated with exercises from Supabase.  
3. Logs saved to the `workout_logs` table with a timestamp.

**Prompt for Copilot:**  
"Create a Streamlit page for logging workouts. Include a dropdown populated with exercises from Supabase, and fields for repetitions, weight, and notes. Validate inputs and save the data to the `workout_logs` table."

---

## Feature: Dashboard

### Objective  
Provide users with an overview of their logged workouts and progress trends.

### Requirements  
- **Summary View:**  
  - Display the latest logged workouts in a list format.  
  - Include details such as exercise name, repetitions, and weight.  

- **Visualization:**  
  - Bar chart for total repetitions per exercise over the past week.  
  - Line chart for weight progression over time for selected exercises.  

- **Backend Integration:**  
  - Fetch data from the `workout_logs` table in Supabase.  
  - Aggregate data for charts (e.g., group logs by week and exercise).  

### Deliverables  
1. A Streamlit page (`dashboard.py`) displaying recent workouts and progress visualizations.  
2. Charts implemented using Streamlit’s charting options (e.g., `st.bar_chart` or `st.line_chart`).  

**Prompt for Copilot:**  
"Create a Streamlit dashboard to display recent workout logs and progress trends. Fetch data from the Supabase `workout_logs` table and display:
- A list of recent workouts.
- A bar chart for weekly repetitions per exercise.
- A line chart for weight progression over time."

---

## Feature: Edit/Delete Exercise

### Objective  
Enable users to update or delete an existing exercise.

### Requirements  
- **Edit:**  
  - Allow users to update the exercise name, type, description, and image.  
  - Replace the old image in Supabase storage if a new one is uploaded.  

- **Delete:**  
  - Remove the exercise from the `exercises` table.  
  - Delete the associated image from the `exercise-images` bucket.  

### Deliverables  
1. A Streamlit page (`edit_delete_exercise.py`) for handling edit and delete operations.  
2. Confirmation dialog for delete operations.  

**Prompt for Copilot:**  
"Create a Streamlit page for editing or deleting exercises. Include inputs to update fields like name, type, description, and image. Use Python to update the Supabase `exercises` table or delete an exercise and its image from the storage bucket. Include a confirmation dialog for deletions."

---

## Feature: Authentication

### Objective  
Allow users to log in and sync their data securely.

### Requirements  
- **Signup/Login:**  
  - Implement email/password authentication using Supabase.  

- **Session Management:**  
  - Persist user sessions using Supabase's built-in session handling.  

### Deliverables  
1. A Streamlit page (`auth.py`) for user authentication.  
2. Session management to protect specific routes.  

**Prompt for Copilot:**  
"Create a Streamlit page for user signup and login using Supabase authentication. Implement session management to protect specific routes and ensure logged-in users can access their data."
