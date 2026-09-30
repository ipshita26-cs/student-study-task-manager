from data_manager import load_data, save_data
from utils import get_non_empty_input, get_positive_number


def add_study_session():
    sessions = load_data("study_sessions.json")

    subject = get_non_empty_input("Enter subject name: ")
    hours = get_positive_number("Enter study time in hours: ")

    session = {
        "subject": subject,
        "hours": hours
    }

    sessions.append(session)
    save_data("study_sessions.json", sessions)

    print("Study session added successfully!")


def view_study_sessions():
    sessions = load_data("study_sessions.json")

    if not sessions:
        print("No study sessions found.")
        return

    print("\n========== STUDY SESSIONS ==========")

    for index, session in enumerate(sessions, start=1):
        print(
            f"{index}. {session['subject']} - "
            f"{session['hours']} hours"
        )

    print("====================================")


def view_total_study_time():
    sessions = load_data("study_sessions.json")

    if not sessions:
        print("No study sessions found.")
        return

    total_hours = 0

    for session in sessions:
        total_hours += session["hours"]

    print(f"\nTotal study time: {total_hours} hours")


def study_menu():
    while True:
        print("\n========== STUDY TRACKER ==========")
        print("1. Add Study Session")
        print("2. View Study Sessions")
        print("3. View Total Study Time")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_study_session()

        elif choice == "2":
            view_study_sessions()

        elif choice == "3":
            view_total_study_time()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")