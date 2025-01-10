# Product Requirements Document: Exercise Tracker Mobile Web App

## Foundation PRD

### Project Setup
**Objective:**  
Establish the foundational structure and tools for the exercise tracker mobile web app.  

**Requirements:**  
- Use **Vanilla JavaScript** as the framework for the web app.  
- Include **Supabase** for cloud storage and authentication.  
- Use **Tailwind CSS** for styling.  
- Add **environment variables** for storing Supabase credentials securely.

**Deliverables:**  
1. A project initialized with a basic HTML, CSS, and JavaScript setup.  
2. A `supabaseClient.js` file that initializes the Supabase client with the project's URL and anon key.  
3. A structured folder setup:
   - `/components/` for reusable JavaScript components.
   - `/pages/` for HTML templates or primary views (e.g., Dashboard, AddExercise).
   - `/assets/` for static files (e.g., styles, images).
   - `/utils/` for utility/helper functions.

**Prompt for Copilot:**  
"Set up a project using Vanilla JavaScript with Tailwind CSS for styling. Install `@supabase/supabase-js` and configure Supabase in a `supabaseClient.js` file using environment variables. Organize folders as `components`, `pages`, `assets`, and `utils` for scalability."

---

## Feature: Add Exercise

### Objective  
Allow users to create exercises with relevant details, including an optional image, and save them to the cloud.

### Requirements  
- **Form Fields:**  
  - Name (text, required).  
  - Type (dropdown: Strength, Cardio, Mobility, required).  
  - Description (textarea, optional).  
  - Image (file input, optional).  

- **Backend Integration:**  
  - Save exercise details to the `exercises` table in Supabase.  
  - Upload image to the Supabase storage bucket `exercise-images`.  
  - Store the image URL in the database.  

- **Validation:**  
  - Ensure all required fields are filled.  
  - Validate image size (<2 MB) and type (JPEG, PNG).

### Deliverables  
1. A JavaScript file (`addExercise.js`) for handling form submission and integrating with Supabase.  
2. An HTML template (`addExercise.html`) containing the form structure styled with Tailwind CSS.  
3. Functionality to upload images to the storage bucket and link their URL to the exercise.  
4. Form validation for required fields and image constraints.  

**Prompt for Copilot:**  
"Create an HTML form styled with Tailwind CSS for adding exercises. Use Vanilla JavaScript to handle form submissions, validate input fields, and save exercise data to the Supabase `exercises` table. Implement image uploads to the `exercise-images` bucket and store the URL in the database."

---

## Feature: View Exercises

### Objective  
Enable users to view all created exercises in a clean and mobile-friendly interface.

### Requirements  
- **UI Elements:**  
  - A grid or list showing the exercise name, type, description, and image.  

- **Backend Integration:**  
  - Fetch data from the `exercises` table in Supabase.  

- **UX Considerations:**  
  - Ensure responsiveness for mobile devices.  

### Deliverables  
1. A JavaScript file (`viewExercises.js`) for fetching and displaying exercise data.  
2. An HTML template (`viewExercises.html`) containing a grid layout styled with Tailwind CSS.  
3. Exercises displayed in a card format showing the name, type, description, and image.  

**Prompt for Copilot:**  
"Create an HTML page styled with Tailwind CSS to display exercises in a responsive grid. Use Vanilla JavaScript to fetch exercise data from the Supabase `exercises` table and populate the grid dynamically with cards showing the exercise name, type, description, and image."

---

## Feature: Log Workout

### Objective  
Allow users to log workout sessions by selecting an exercise and tracking repetitions, weights, and notes.

### Requirements  
- **Form Fields:**  
  - Dropdown to select an exercise (populated from the `exercises` table).  
  - Repetitions (integer, required).  
  - Weight (float, required).  
  - Notes (textarea, optional).  

- **Backend Integration:**  
  - Save workout logs to the `workout_logs` table in Supabase.  

- **Validation:**  
  - Ensure repetitions and weight are positive numbers.

### Deliverables  
1. A JavaScript file (`logWorkout.js`) for handling form submission and integrating with Supabase.  
2. An HTML template (`logWorkout.html`) containing the form structure styled with Tailwind CSS.  
3. Dropdown dynamically populated with exercises from Supabase.  
4. Logs saved to the `workout_logs` table with a timestamp.

**Prompt for Copilot:**  
"Create an HTML form styled with Tailwind CSS for logging workouts. Use Vanilla JavaScript to populate a dropdown with exercises from the Supabase `exercises` table, validate input fields, and save workout data to the `workout_logs` table."

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
1. A JavaScript file (`dashboard.js`) for fetching and displaying workout data.  
2. An HTML template (`dashboard.html`) containing a summary view styled with Tailwind CSS.  
3. Charts implemented using a library like Chart.js.  

**Prompt for Copilot:**  
"Create an HTML page styled with Tailwind CSS to display a workout summary dashboard. Use Vanilla JavaScript to fetch workout data from the Supabase `workout_logs` table and display:
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
1. A JavaScript file (`editDeleteExercise.js`) for handling edit and delete operations.  
2. An HTML template (`editDeleteExercise.html`) containing the interface styled with Tailwind CSS.  
3. Confirmation dialog for delete operations.  

**Prompt for Copilot:**  
"Create an HTML page styled with Tailwind CSS for editing or deleting exercises. Use Vanilla JavaScript to update exercise data in the Supabase `exercises` table or delete an exercise and its image from the storage bucket. Include a confirmation dialog for deletions."

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
1. A JavaScript file (`auth.js`) for handling user authentication.  
2. HTML templates (`login.html`, `signup.html`) containing forms styled with Tailwind CSS.  
3. Authentication state management for protected routes.

**Prompt for Copilot:**  
"Create HTML forms styled with Tailwind CSS for user signup and login. Use Vanilla JavaScript to handle authentication with Supabase, manage user sessions, and protect specific routes."
