# Task-Manager

Django Task Manager is a simple web application for managing tasks. Users can create, list, and delete tasks with associated titles, descriptions, deadlines, and priorities.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eps-zero/Task-Manager.git
   cd Task-Manager
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser account to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your web browser and navigate to `http://localhost:8000/admin/` to access the admin panel and manage tasks.

## Usage

### Task List

- The default landing page displays a list of all tasks.
- You can delete a task by clicking the "Delete" button next to it.

### Create Task

- To create a new task, go to `http://localhost:8000/create/` or click the "Create Task" link on the task list page.
- Fill in the task details, including title, description, deadline, and priority.
- Click the "Create Task" button to add the task.

### Delete Task

- To delete a specific task, go to `http://localhost:8000/delete/<task_id>/`, where `<task_id>` is the ID of the task you want to delete.
- Confirm the deletion when prompted.
