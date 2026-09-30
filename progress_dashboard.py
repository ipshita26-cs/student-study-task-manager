from data_manager import load_data


def show_dashboard():
    tasks = load_data("tasks.json")
    sessions = load_data("study_sessions.json")
    marks = load_data("marks.json")

    completed_tasks = 0

    for task in tasks:
        if task["status"] == "Completed":
            completed_tasks += 1

    pending_tasks = len(tasks) - completed_tasks

    total_study_hours = 0

    for session in sessions:
        total_study_hours += session["hours"]

    total_marks = 0

    for subject in marks:
        total_marks += subject["marks"]

    if marks:
        average_marks = total_marks / len(marks)
    else:
        average_marks = 0

    print("\n========================================")
    print("          PROGRESS DASHBOARD")
    print("========================================")

    print(f"Total Tasks       : {len(tasks)}")
    print(f"Completed Tasks   : {completed_tasks}")
    print(f"Pending Tasks     : {pending_tasks}")

    print(f"Total Study Time  : {total_study_hours} hours")

    print(f"Subjects Recorded : {len(marks)}")
    print(f"Average Marks     : {average_marks:.2f}/100")

    print("========================================\n")