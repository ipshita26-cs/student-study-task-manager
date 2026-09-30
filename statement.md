# Project Statement

## Project Title

Student Study & Task Manager

---

## 1. Introduction

Students need to manage several academic activities such as assignments, study time, and examination marks. Managing these activities separately can make it difficult to keep track of academic progress.

The Student Study & Task Manager is a console-based Python application that provides a simple solution for managing these activities in one place.

---

## 2. Problem Statement

Students may have multiple tasks, study sessions, and subject marks to keep track of. Without a simple organized system, it can become difficult to monitor pending work, study time, and academic performance.

The aim of this project is to develop a simple Python-based application that allows students to manage these activities through a single menu-driven system.

---

## 3. Proposed Solution

The proposed system provides four main functional modules:

1. Task Manager
2. Study Tracker
3. Marks Manager
4. Progress Dashboard

The application uses JSON files to store information so that data remains available when the program is restarted.

---

## 4. Objectives

The objectives of this project are:

- To provide a simple system for managing student tasks.
- To record and monitor study sessions.
- To store and calculate subject marks.
- To provide a summary of academic progress.
- To demonstrate fundamental Python programming concepts.
- To implement input validation and basic error handling.
- To use modular programming by dividing functionality into separate Python files.
- To provide persistent data storage using JSON files.

---

## 5. Scope

The project is intended for students who want a simple way to organize basic academic information.

The current scope includes:

- Academic task management
- Study time tracking
- Subject mark management
- Average mark calculation
- Basic progress summary
- Local JSON-based data storage

The current version does not include online accounts, cloud storage, databases, or graphical interfaces.

---

## 6. Functional Requirements

### FR1 - Task Management

The system shall allow the user to:

- Add a task.
- View existing tasks.
- Mark a task as completed.
- Delete a task.

### FR2 - Study Tracking

The system shall allow the user to:

- Add a study session.
- Enter the subject studied.
- Enter the number of hours studied.
- View recorded study sessions.
- Calculate total study time.

### FR3 - Marks Management

The system shall allow the user to:

- Add marks for a subject.
- View recorded marks.
- Calculate average marks.
- Reject marks outside the range of 0 to 100.

### FR4 - Progress Dashboard

The system shall display:

- Total number of tasks.
- Number of completed tasks.
- Number of pending tasks.
- Total study time.
- Number of subjects with recorded marks.
- Average marks.

### FR5 - Data Storage

The system shall store task, study-session, and marks information in JSON files.

---

## 7. Non-Functional Requirements

### NFR1 - Usability

The application should provide a simple menu-driven interface that is easy for a student to understand and operate.

### NFR2 - Reliability

The application should handle common invalid inputs without terminating unexpectedly.

### NFR3 - Maintainability

The application should be divided into separate modules and functions so that individual components can be understood and modified easily.

### NFR4 - Data Persistence

The application should retain stored information after the program is closed and restarted.

### NFR5 - Portability

The application should run on systems that have Python installed without requiring external Python libraries.

---

## 8. Technologies Used

- Python
- JSON
- Visual Studio Code
- Git
- GitHub

---

## 9. Python Concepts Used

The project demonstrates the following fundamental Python concepts:

- Variables
- Data types
- Input and output
- Strings
- Conditional statements
- Loops
- Lists
- Dictionaries
- Functions
- Exception handling
- File handling
- JSON data storage
- Modular programming

---

## 10. Module Description

### Task Manager

Responsible for creating, displaying, completing, and deleting tasks.

### Study Tracker

Responsible for recording study sessions and calculating total study time.

### Marks Manager

Responsible for recording marks and calculating the average.

### Progress Dashboard

Reads information from the stored data and presents an overall summary.

### Data Manager

Provides functions for loading and saving JSON data.

### Utilities

Provides reusable functions for input validation.

### Main Module

Provides the main menu and connects all modules.

---

## 11. Data Files

The application uses three JSON files:

- `tasks.json` - stores task information.
- `study_sessions.json` - stores study-session information.
- `marks.json` - stores subject marks.

---

## 12. Validation and Error Handling

The system includes validation for common user input errors.

Examples include:

- Empty input is rejected where necessary.
- Invalid numerical input is handled.
- Study hours must be greater than zero.
- Marks must be between 0 and 100.
- Invalid menu choices are handled.
- Invalid task numbers are rejected.

---

## 13. Expected Outcome

The completed system should provide students with a simple console-based application for managing tasks, tracking study time, recording marks, and viewing a basic academic progress summary.

The project also demonstrates how fundamental Python concepts can be combined to create a modular and functional application.

---

## 14. Conclusion

The Student Study & Task Manager is designed as a simple academic management application using fundamental Python programming concepts.

The project combines multiple related functions into one modular system while using JSON files for persistent local storage. It provides a practical application of Python concepts learned during the course.