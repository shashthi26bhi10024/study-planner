"""
main.py - Main entry point and CLI interface for Study Planner.

This module demonstrates:
- Input and output operations (input(), print())
- Control flow:
  - while True main menu loop
  - if-elif-else branching
  - nested conditions
  - break and continue
- Function definitions and calls
- Module imports (planner, utils)
- Clean, realistic first-year student coding style
"""

import planner
import utils


def display_menu():
    """
    Displays the standard command-line menu.
    Demonstrates print() and string formatting.
    """
    print("\n========================================")
    print("           STUDY PLANNER")
    print("========================================")
    print("1. Add Study Task")
    print("2. View All Tasks")
    print("3. Search Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. View Tasks by Subject")
    print("7. View Pending Tasks")
    print("8. View Completed Tasks")
    print("9. Study Summary")
    print("10. Exit")
    print("========================================")


def handle_add_task(study_planner):
    """
    Handles menu option 1: Add Study Task.
    Prompts for subject, topic, duration, priority, and optional tags.
    """
    utils.print_header("Add New Study Task")

    # Input validation for subject and topic using while loops
    subject = utils.get_non_empty_string("Enter Subject (e.g., Python, Math, Physics): ")
    topic = utils.get_non_empty_string("Enter Topic (e.g., Functions, Matrices): ")

    # Input validation for duration (positive integer between 5 and 720 minutes)
    duration = utils.get_valid_integer(
        "Enter Planned Duration in minutes (5 - 720): ",
        min_val=5,
        max_val=720
    )

    # Validated priority selection
    priority = utils.get_valid_priority()

    # Optional study attribute flags (demonstrates bitwise encoding)
    print("\nOptional Attributes (Enter 'y' for Yes, or press Enter for No):")
    is_exam_input = input("Is this an Exam/Important topic? (y/n): ").strip().lower()
    is_exam = (is_exam_input == "y" or is_exam_input == "yes")

    is_rev_input = input("Does this require revision? (y/n): ").strip().lower()
    is_rev = (is_rev_input == "y" or is_rev_input == "yes")

    is_prac_input = input("Is this a practical/lab exercise? (y/n): ").strip().lower()
    is_prac = (is_prac_input == "y" or is_prac_input == "yes")

    flags = utils.encode_study_flags(
        is_revision=is_rev,
        is_important=is_exam,
        is_practical=is_prac
    )

    # Add task to planner
    new_task = study_planner.add_task(
        subject=subject,
        topic=topic,
        duration=duration,
        priority=priority,
        flags=flags
    )

    print("\nSuccess: Study Task added successfully!")
    print(f"Assigned Task ID: {new_task.task_id}")

    # Optional demonstration of type() for course requirements
    show_types = input("Inspect variable types for this task? (y/n) [Default: n]: ").strip().lower()
    if show_types == "y" or show_types == "yes":
        utils.inspect_task_types(new_task)


def handle_view_all(study_planner):
    """
    Handles menu option 2: View All Tasks.
    Demonstrates for loop, iteration over list, and conditional check.
    """
    utils.print_header("All Study Tasks")
    tasks = study_planner.get_all_tasks()

    if len(tasks) == 0:
        print("No study tasks found. Use Option 1 to add a task.")
        return

    print(f"Total Tasks in Planner: {len(tasks)}\n")
    for task in tasks:
        print(utils.format_task_row(task))
    utils.print_divider()


def handle_search(study_planner):
    """
    Handles menu option 3: Search Task.
    Searches by Task ID, Subject, or Topic using membership operators.
    """
    utils.print_header("Search Study Tasks")
    query = input("Enter search term (Task ID, Subject, or Topic): ").strip()

    if not query:
        print("Error: Search query cannot be empty.")
        return

    results = study_planner.search_tasks(query)

    if len(results) == 0:
        print(f"No tasks found matching '{query}'.")
    else:
        print(f"\nFound {len(results)} matching task(s):")
        for task in results:
            task.display_details()


def handle_mark_completed(study_planner):
    """
    Handles menu option 4: Mark Task as Completed.
    Validates task existence and updates status.
    """
    utils.print_header("Mark Task as Completed")
    task_id = utils.get_valid_integer("Enter Task ID to mark as completed: ", min_val=1)

    task = study_planner.find_task_by_id(task_id)

    # Identity operator check
    if task is None:
        print(f"Error: Task with ID {task_id} does not exist.")
        return

    if task.status == "Completed":
        print(f"Notice: Task ID {task_id} ('{task.topic}') is ALREADY marked as Completed!")
    else:
        task.mark_completed()
        print(f"Great job! Task ID {task_id} ('{task.topic}') has been marked as COMPLETED [✓].")


def handle_delete_task(study_planner):
    """
    Handles menu option 5: Delete Task.
    Confirms deletion before removing task from list.
    """
    utils.print_header("Delete Study Task")
    task_id = utils.get_valid_integer("Enter Task ID to delete: ", min_val=1)

    task = study_planner.find_task_by_id(task_id)

    if task is None:
        print(f"Error: Task with ID {task_id} not found.")
        return

    # Display task details for confirmation
    print(f"\nYou selected: ID {task.task_id} - {task.subject}: {task.topic}")
    confirm = input("Are you sure you want to delete this task? (y/n): ").strip().lower()

    if confirm == "y" or confirm == "yes":
        deleted = study_planner.delete_task(task_id)
        if deleted:
            print(f"Success: Task ID {task_id} has been permanently deleted.")
        else:
            print("Error: Could not delete task.")
    else:
        print("Deletion cancelled. Task was not deleted.")


def handle_view_by_subject(study_planner):
    """
    Handles menu option 6: View Tasks by Subject.
    Demonstrates set operations for listing unique subjects.
    """
    utils.print_header("View Tasks by Subject")

    unique_subjects = study_planner.get_unique_subjects()

    if len(unique_subjects) == 0:
        print("No tasks or subjects currently available.")
        return

    print("Existing subjects in your planner:")
    # Demonstrates set iteration with a for loop
    for subj in sorted(unique_subjects):
        print(f" - {subj}")
    print()

    selected_subject = utils.get_non_empty_string("Enter subject name to filter: ")
    filtered_tasks = study_planner.get_tasks_by_subject(selected_subject)

    if len(filtered_tasks) == 0:
        print(f"No tasks found for subject '{selected_subject}'.")
    else:
        print(f"\nTasks for '{selected_subject}' ({len(filtered_tasks)} found):")
        for task in filtered_tasks:
            print(utils.format_task_row(task))
    utils.print_divider()


def handle_view_pending(study_planner):
    """
    Handles menu option 7: View Pending Tasks.
    """
    utils.print_header("Pending Study Tasks")
    pending = study_planner.get_pending_tasks()

    if len(pending) == 0:
        print("Awesome! You have no pending study tasks.")
    else:
        print(f"You have {len(pending)} pending task(s):\n")
        for task in pending:
            print(utils.format_task_row(task))
    utils.print_divider()


def handle_view_completed(study_planner):
    """
    Handles menu option 8: View Completed Tasks.
    """
    utils.print_header("Completed Study Tasks")
    completed = study_planner.get_completed_tasks()

    if len(completed) == 0:
        print("No completed tasks yet. Finish a task and mark it complete!")
    else:
        print(f"You have completed {len(completed)} task(s):\n")
        for task in completed:
            print(utils.format_task_row(task))
    utils.print_divider()


def handle_summary(study_planner):
    """
    Handles menu option 9: Study Summary.
    Displays calculations using arithmetic, array, mixed division, and dictionary.
    """
    utils.print_header("Study Progress Summary")
    summary = study_planner.calculate_summary()

    if summary["total_tasks"] == 0:
        print("No tasks to summarize. Please add tasks first.")
        return

    # Display calculated metrics
    print(f"Total Tasks Recorded       : {summary['total_tasks']}")
    print(f"Completed Tasks            : {summary['completed_tasks']} [✓]")
    print(f"Pending Tasks              : {summary['pending_tasks']} [ ]")
    print(f"Completion Rate            : {summary['completion_percentage']}%")
    utils.print_divider()

    print("Study Time Analysis (using Python array & mixed division):")
    print(f"Total Planned Time         : {summary['total_minutes']} minutes")
    print(f"Formatted Duration         : {summary['hours']} hours and {summary['remaining_minutes']} minutes")
    print(f"Decimal Equivalent         : {summary['decimal_hours']} hours")
    print(f"Average Time Per Task      : {summary['average_minutes']} minutes")
    print(f"Shortest Task Duration     : {summary['min_duration']} minutes")
    print(f"Longest Task Duration      : {summary['max_duration']} minutes")
    utils.print_divider()

    print(f"Total Unique Subjects      : {summary['unique_subjects_count']} (via Python set)")
    print("Priority Breakdown (via Python dictionary):")
    for priority, count in summary["priority_breakdown"].items():
        print(f" - {priority:<6}: {count} task(s)")
    utils.print_divider()


def main():
    """
    Main function executing the Study Planner CLI.
    Demonstrates:
    - Object instantiation: StudyPlanner()
    - Infinite while loop (while True)
    - User input handling
    - Control flow with if-elif-else
    - break statement for graceful program exit
    """
    planner_app = planner.StudyPlanner()

    print("\nWelcome to the Study Planner!")
    print("A command-line task organizer for student studies.")

    while True:
        display_menu()
        choice = input("Enter your choice (1-10): ").strip()

        # Control flow branching
        if choice == "1":
            handle_add_task(planner_app)
        elif choice == "2":
            handle_view_all(planner_app)
        elif choice == "3":
            handle_search(planner_app)
        elif choice == "4":
            handle_mark_completed(planner_app)
        elif choice == "5":
            handle_delete_task(planner_app)
        elif choice == "6":
            handle_view_by_subject(planner_app)
        elif choice == "7":
            handle_view_pending(planner_app)
        elif choice == "8":
            handle_view_completed(planner_app)
        elif choice == "9":
            handle_summary(planner_app)
        elif choice == "10" or choice.lower() == "exit":
            print("\nThank you for using Study Planner. Happy studying!")
            print("Exiting application...\n")
            break
        else:
            print("\n[!] Invalid selection. Please enter a valid number between 1 and 10.")


# Standard Python entry point
if __name__ == "__main__":
    main()
