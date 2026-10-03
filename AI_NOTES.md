AI Prompt
create a command-line task-duration tracker. The user enters a task name and positive whole-number minutes for each task. A blank task name ends entry. The program displays total minutes and the task with the longest duration. Use only the Python standard library and keep the code beginner-readable.

AI Response (Gemini)
Here is a clean, beginner-friendly Python script using only the standard library.
Python
def main():
    tasks = []

    print("--- Task Duration Tracker ---")
    print("Enter a task name, then its duration in minutes.")
    print("Press Enter on a blank task name when you are finished.\n")

    while True:
        # Get task name
        task_name = input("Enter task name: ").strip()

        # A blank task name ends entry
        if not task_name:
            break

        # Validate that the duration is a positive whole number
        while True:
            duration_input = input(
                f"Enter duration in minutes for '{task_name}': "
            ).strip()

            if duration_input.isdigit() and int(duration_input) > 0:
                duration = int(duration_input)
                break
            else:
                print(
                    "Invalid input. Please enter a positive whole number (e.g., 15, 30)."
                )

        # Store task as a dictionary
        tasks.append({"name": task_name, "duration": duration})
        print()

    # Handle case where no tasks were entered
    if not tasks:
        print("\nNo tasks were entered.")
        return

    # Calculate summary statistics
    total_minutes = sum(task["duration"] for task in tasks)
    longest_task = max(tasks, key=lambda task: task["duration"])

    # Display results
    print("\n" + "=" * 30)
    print("       SUMMARY REPORT       ")
    print("=" * 30)
    print(f"Total tasks entered : {len(tasks)}")
    print(f"Total time spent    : {total_minutes} minutes")
    print(
        f"Longest task        : {longest_task['name']} ({longest_task['duration']} minutes)"
    )
    print("=" * 30)


if __name__ == "__main__":
    main()
Key Highlights
•	Validation: .isdigit() and int(duration_input) > 0 ensure only positive whole numbers are accepted for time entries.
•	Data Storage: Tasks are kept in a list of dictionaries, making fields easily readable (e.g., task["duration"]).
•	Built-in Functions: sum() calculates total runtime effortlessly, while max() finds the task with the highest duration value.

