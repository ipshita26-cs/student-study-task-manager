from data_manager import load_data, save_data
from utils import get_non_empty_input, get_mark


def add_marks():
    marks = load_data("marks.json")

    subject = get_non_empty_input("Enter subject name: ")
    mark = get_mark("Enter marks (0-100): ")

    subject_marks = {
        "subject": subject,
        "marks": mark
    }

    marks.append(subject_marks)
    save_data("marks.json", marks)

    print("Marks added successfully!")


def view_marks():
    marks = load_data("marks.json")

    if not marks:
        print("No marks found.")
        return

    print("\n========== MARKS ==========")

    for index, subject in enumerate(marks, start=1):
        print(f"{index}. {subject['subject']} - {subject['marks']}/100")

    print("===========================")


def calculate_average():
    marks = load_data("marks.json")

    if not marks:
        print("No marks found.")
        return

    total_marks = 0

    for subject in marks:
        total_marks += subject["marks"]

    average = total_marks / len(marks)

    print(f"\nAverage marks: {average:.2f}/100")


def marks_menu():
    while True:
        print("\n========== MARKS MANAGER ==========")
        print("1. Add Marks")
        print("2. View Marks")
        print("3. Calculate Average")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_marks()

        elif choice == "2":
            view_marks()

        elif choice == "3":
            calculate_average()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")