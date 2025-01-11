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

## Feature: Workouts Containing Multiple Exercises with Series

### Objective  
Allow users to log workouts consisting of multiple exercises. Each exercise can have multiple series (sets) with repetitions and associated weights.

### Requirements  
- **Hierarchy:**
  - A workout groups multiple exercises.
  - Each exercise within a workout can contain multiple series.

- **Input Fields:**  
  - **Workout Details:**
    - Name (optional, e.g., "Leg Day").
    - Date (required).
    - Notes (optional).
  - **Exercise Details:**
    - Exercise Name (selected from predefined list).
    - Weight (per exercise, optional).
    - Notes (optional).
  - **Series Details:**
    - Repetitions (integer, required).

- **Backend Integration:**  
  - Store workouts in the `workouts` table.
  - Associate exercises with workouts in the `workout_exercises` table.
  - Track series (sets) for each exercise in the `series` table.

### Deliverables  
1. A Streamlit page (`log_workout.py`) for logging workouts, exercises, and series.
2. A relational database schema:
    - `workouts` table to track each workout session.
    - `workout_exercises` table to associate exercises with workouts.
    - `series` table to track series for each exercise.

**Prompt for Copilot:**  
"Create a Streamlit page for logging workouts. Allow users to:
- Add a workout with a name, date, and notes.
- Add multiple exercises to the workout, each with weight and notes.
- Log series (sets) for each exercise with repetitions and associated weights. Save the data into relational tables: `workouts`, `workout_exercises`, and `series`."

---

## Feature: Add Exercise

### Objective  
Allow users to create predefined exercises with relevant details, including an optional image, and save them to the cloud.

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

## Feature: View Workouts and Exercises

### Objective  
Enable users to view logged workouts and their associated exercises and series in a hierarchical format.

### Requirements  
- **UI Elements:**  
  - List of workouts with name, date, and notes.  
  - For each workout, show associated exercises with name, weight, and notes.  
  - For each exercise, list its series (sets) with repetitions and weights.  

- **Backend Integration:**  
  - Fetch data from the `workouts`, `workout_exercises`, and `series` tables in Supabase.  

### Deliverables  
1. A Streamlit page (`view_workouts.py`) for fetching and displaying workout data.  
2. Hierarchical display format:
    - Workouts > Exercises > Series.  

**Prompt for Copilot:**  
"Create a Streamlit page to view workouts. Display a list of workouts with associated exercises and their series. Fetch data from the `workouts`, `workout_exercises`, and `series` tables in Supabase."

---

## Feature: Dashboard

### Objective  
Provide users with an overview of their workout progress, including metrics on exercises and series logged over time.

### Requirements  
- **Summary View:**  
  - Display total workouts, exercises, and series logged.  
  - Show metrics like average repetitions, total weight lifted, and most used exercises.  

- **Visualization:**  
  - Line chart for workout frequency over time.  
  - Bar chart for total weight lifted per exercise.  

- **Backend Integration:**  
  - Fetch data from the `workouts`, `workout_exercises`, and `series` tables.  

### Deliverables  
1. A Streamlit page (`dashboard.py`) displaying workout metrics and visualizations.  
2. Charts implemented using Streamlit’s charting options (e.g., `st.bar_chart`, `st.line_chart`).  

**Prompt for Copilot:**  
"Create a Streamlit dashboard to display workout progress. Include metrics on total workouts, exercises, and series logged. Visualize workout frequency and total weight lifted using charts. Fetch data from the `workouts`, `workout_exercises`, and `series` tables in Supabase."

---

## Feature: Edit/Delete Workout or Exercise

### Objective  
Enable users to update or delete an existing workout, its exercises, or their series.

### Requirements  
- **Edit:**  
  - Allow users to update workout details (name, date, notes).
  - Modify exercises in the workout (weight, notes).
  - Update series (repetitions, weights).  

- **Delete:**  
  - Remove a workout and its associated exercises and series.  
  - Remove an exercise and its series from a workout.  

### Deliverables  
1. A Streamlit page (`edit_delete_workout.py`) for handling edit and delete operations.  
2. Confirmation dialog for delete operations.  

**Prompt for Copilot:**  
"Create a Streamlit page to edit or delete workouts and their associated exercises or series. Include inputs to update fields and provide confirmation dialogs for deletions. Use Python to update or delete data in the `workouts`, `workout_exercises`, and `series` tables."
