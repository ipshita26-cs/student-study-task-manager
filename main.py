from task_manager import task_menu
from study_tracker import study_menu
from marks_manager import marks_menu
from progress_dashboard import show_dashboard


def main():
    while True:
        print("\n========================================")
        print("      STUDENT STUDY & TASK MANAGER")
        print("========================================")
        print("1. Task Manager")
        print("2. Study Tracker")
        print("3. Marks Manager")
        print("4. Progress Dashboard")
        print("5. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_menu()

        elif choice == "2":
            study_menu()

        elif choice == "3":
            marks_menu()

        elif choice == "4":
            show_dashboard()

        elif choice == "5":
            print("Thank you for using Student Study & Task Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()