# 📘 Assignment: To-Do Tracker

## 🎯 Objective

Build a small personal task tracker in Python that saves tasks in a database and lets the user add, view, update, and remove items. This assignment helps students practice working with data, functions, and simple project organization.

## 📝 Tasks

### 🛠️ Create the Database

#### Description
Create a Python program that sets up a SQLite database for a to-do list. The database should store each task with a title, a completion status, and a due date.

#### Requirements
Completed program should:

- Create a SQLite database file named `tasks.db`
- Create a table named `tasks`
- Store at least these fields: `id`, `title`, `completed`, and `due_date`
- Add a function to initialize the database when the program starts

### 🛠️ Add and View Tasks

#### Description
Allow the user to add new tasks and display all tasks currently stored in the database.

#### Requirements
Completed program should:

- Include a function to add a new task
- Prompt the user for a task title and due date
- Include a function to list all tasks in a readable format
- Show whether each task is complete or incomplete

### 🛠️ Update and Remove Tasks

#### Description
Expand the program so users can mark a task as complete or delete a task they no longer need.

#### Requirements
Completed program should:

- Add a function to mark a task as completed
- Add a function to delete a task by ID
- Validate user input to prevent invalid task numbers
- Print a confirmation message after each update or deletion

### 🛠️ Final Project Flow

#### Description
Create a simple menu-driven app that lets a user interact with the tracker from the terminal.

#### Requirements
Completed program should:

- Display a menu with options such as add, view, complete, delete, and exit
- Keep running until the user chooses to exit
- Save data so it remains available after the program closes
- Use clear messages and clean formatting for the output
