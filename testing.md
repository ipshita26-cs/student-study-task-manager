# Testing Documentation

## 1. Testing Overview

The Student Study & Task Manager was tested using different valid and invalid inputs to verify that the application functions correctly and handles common input errors.

Testing was performed by running:

python main.py

---

## 2. Test Cases

### TC01 - Main Menu - Task Manager

Test Description:
Select Task Manager from the main menu.

Input:
1

Expected Result:
Task Manager opens successfully.

Status:
Passed

---

### TC02 - Main Menu - Study Tracker

Test Description:
Select Study Tracker from the main menu.

Input:
2

Expected Result:
Study Tracker opens successfully.

Status:
Passed

---

### TC03 - Main Menu - Marks Manager

Test Description:
Select Marks Manager from the main menu.

Input:
3

Expected Result:
Marks Manager opens successfully.

Status:
Passed

---

### TC04 - Main Menu - Progress Dashboard

Test Description:
Select Progress Dashboard from the main menu.

Input:
4

Expected Result:
Progress Dashboard opens successfully.

Status:
Passed

---

### TC05 - Main Menu - Invalid Choice

Test Description:
Enter an invalid menu choice.

Input:
9

Expected Result:
An invalid choice message is displayed and the user is returned to the menu.

Status:
Passed

---

### TC06 - Task Manager - Add Task

Test Description:
Add a new task.

Input:
A valid task name.

Expected Result:
The task is added successfully and stored in the tasks JSON file.

Status:
Passed

---

### TC07 - Task Manager - View Tasks

Test Description:
View the stored tasks.

Input:
Option 2 in Task Manager.

Expected Result:
The stored tasks are displayed with their status.

Status:
Passed

---

### TC08 - Task Manager - Complete Task

Test Description:
Mark a task as completed.

Input:
A valid task number.

Expected Result:
The selected task status changes from Pending to Completed.

Status:
Passed

---

### TC09 - Task Manager - Delete Task

Test Description:
Delete an existing task.

Input:
A valid task number.

Expected Result:
The selected task is deleted successfully.

Status:
Passed

---

### TC10 - Study Tracker - Add Study Session

Test Description:
Add a study session.

Input:
A valid subject name and study time.

Expected Result:
The study session is stored successfully.

Status:
Passed

---

### TC11 - Study Tracker - Invalid Study Time

Test Description:
Enter non-numeric study time.

Input:
abc

Expected Result:
The system displays an invalid number message and asks for valid input.

Status:
Passed

---

### TC12 - Study Tracker - Negative Study Time

Test Description:
Enter a negative study time.

Input:
-2

Expected Result:
The system rejects the value and asks for a positive number.

Status:
Passed

---

### TC13 - Marks Manager - Add Valid Marks

Test Description:
Add marks within the valid range.

Input:
85

Expected Result:
The marks are stored successfully.

Status:
Passed

---

### TC14 - Marks Manager - Marks Above Range

Test Description:
Enter marks greater than 100.

Input:
105

Expected Result:
The system rejects the input because marks must be between 0 and 100.

Status:
Passed

---

### TC15 - Marks Manager - Negative Marks

Test Description:
Enter negative marks.

Input:
-5

Expected Result:
The system rejects the input because marks cannot be negative.

Status:
Passed

---

### TC16 - Marks Manager - Calculate Average

Test Description:
Calculate the average of stored marks.

Input:
Stored marks for subjects.

Expected Result:
The application calculates and displays the average marks.

Status:
Passed

---

### TC17 - Progress Dashboard - Empty Data

Test Description:
Display the dashboard when the JSON files contain no data.

Input:
Empty JSON files.

Expected Result:
All relevant values are displayed as zero.

Status:
Passed

---

### TC18 - Data Storage - Data Persistence

Test Description:
Check whether stored data remains available after restarting the application.

Input:
Previously stored tasks, study sessions, or marks.

Expected Result:
Previously stored data remains available after restarting the application.

Status:
Passed

---

## 3. Validation Testing

### Invalid Marks

The system was tested with marks outside the valid range.

Example:

Enter marks (0-100): -5

Expected behavior:

Marks must be between 0 and 100.

The system correctly rejected the invalid value and requested valid input.

A value greater than 100 was also tested and rejected.

---

### Invalid Study Time

The system was tested with non-numeric study time.

Example:

Enter study time in hours: abc

The system displayed an error message instead of terminating.

Negative study time was also tested and rejected.

---

### Invalid Menu Choice

The main menu was tested with an invalid choice.

Example:

Enter your choice: 9

The application displayed an invalid-choice message and returned to the menu.

---

## 4. Data Persistence Testing

Data persistence was tested by performing the following steps:

1. Add information to the application.
2. Save the information.
3. Close the application.
4. Run the application again.
5. View the previously stored information.

The application uses JSON files to store data, allowing previously saved information to remain available after restarting the application.

---

## 5. Dashboard Testing

The Progress Dashboard was tested with empty data files.

Expected output:

Total Tasks       : 0
Completed Tasks   : 0
Pending Tasks     : 0
Total Study Time  : 0 hours
Subjects Recorded : 0
Average Marks     : 0.00/100

The dashboard displayed the expected values.

---

## 6. Testing Result

The Student Study & Task Manager was tested using valid and invalid inputs.

The testing confirmed that the application:

- Provides access to all four main modules.
- Validates important user inputs.
- Handles invalid menu choices.
- Stores data using JSON files.
- Retains stored data after restarting the application.
- Calculates and displays progress information.

The tested functionality worked as expected for the tested inputs.