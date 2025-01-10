# Product Requirements Document: Exercise Tracker Mobile Web App

## Foundation PRD

### Project Setup
**Objective:**  
Establish the foundational structure and tools for the exercise tracker mobile web app.  

**Requirements:**  
- Use **Svelte** as the framework for the web app.  
- Include **Supabase** for cloud storage and authentication.  
- Use **SvelteKit** for routing and server-side rendering.  
- Add **environment variables** for storing Supabase credentials securely.

**Deliverables:**  
1. A Svelte project scaffolded using `npm create svelte@latest`.  
2. A `supabaseClient.js` file that initializes the Supabase client with the project's URL and anon key.  
3. A structured folder setup:
   - `/src/components/` for reusable components.
   - `/src/routes/` for page-level views (e.g., Dashboard, AddExercise).
   - `/src/lib/` for utility/helper functions.
   - `/src/assets/` for static files (e.g., images and styles).

**Prompt for Copilot:**  
"Set up a SvelteKit project for a mobile web app. Install `@supabase/supabase-js` and configure Supabase in a `supabaseClient.js` file using environment variables. Organize folders as `components`, `routes`, `lib`, and `assets` for scalability."

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
1. A Svelte component called `AddExercise.svelte` with a form for the above fields.  
2. Functionality to upload images to the storage bucket and link their URL to the exercise.  
3. Form validation for required fields and image constraints.  

**Prompt for Copilot:**  
"Create a Svelte component `AddExercise.svelte` with a form to add exercises. Include fields for name, type (dropdown), description, and an image upload. Save the data to the Supabase `exercises` table, upload the image to the `exercise-images` bucket, and store the URL in the database. Validate required fields and ensure the image size is under 2 MB."

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
1. A Svelte component called `ViewExercises.svelte` that fetches and displays all exercises.  
2. Exercises should be displayed in a card layout, showing the name, type, description, and image.  

**Prompt for Copilot:**  
"Create a Svelte component `ViewExercises.svelte` to fetch and display all exercises from the Supabase `exercises` table. Show each exercise in a responsive card layout with the name, type, description, and image."

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
1. A Svelte component called `LogWorkout.svelte` with a form for the above fields.  
2. Dropdown dynamically populated with exercises from Supabase.  
3. Logs saved to the `workout_logs` table with a timestamp.

**Prompt for Copilot:**  
"Create a Svelte component `LogWorkout.svelte` with a form to log workouts. Include a dropdown populated from the Supabase `exercises` table, fields for repetitions (integer), weight (float), and optional notes. Save the log to the `workout_logs` table with the current timestamp."

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
1. A Svelte component called `Dashboard.svelte` with the latest logs and visualizations.  
2. Use a charting library (e.g., ApexCharts or Chart.js) for bar and line charts.  

**Prompt for Copilot:**  
"Create a Svelte component `Dashboard.svelte` for a workout summary. Fetch workout logs from the `workout_logs` table in Supabase. Display the latest logs in a list and include a bar chart for weekly repetitions per exercise and a line chart for weight progression over time."

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
1. A Svelte component or modal for editing exercises.  
2. Delete functionality with a confirmation step.  

**Prompt for Copilot:**  
"Create functionality to edit or delete exercises in Svelte. Allow users to update fields like name, type, description, and image. Replace the old image in Supabase storage when uploading a new one. For deletion, remove the exercise from the `exercises` table and its image from the `exercise-images` bucket."

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
1. A Svelte component for login/signup forms.  
2. Authentication state management to protect routes like `LogWorkout` and `Dashboard`.

**Prompt for Copilot:**  
"Create an authentication flow in Svelte using Supabase. Implement email/password signup and login, and use Supabase's session management to maintain login state. Protect app routes based on user authentication status."
