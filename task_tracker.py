def add_task(tasks):
    """Handles adding a new task or combining duration with an existing one."""
    task_name = input("Enter task name: ").strip()
    if not task_name:
        return

    # Check for duplicate task names (case-insensitive)
    existing_task = next(
        (t for t in tasks if t["name"].lower() == task_name.lower()), None
    )

    if existing_task:
        print(f"Note: '{existing_task['name']}' already exists with {existing_task['duration']} mins.")
        action = input("Combine duration with existing task? [y/n]: ").strip().lower()

        if action == "y":
            while True:
                duration_input = input(
                    f"Enter additional minutes to add to '{existing_task['name']}': "
                ).strip()
                try:
                    additional_duration = int(duration_input)
                    if additional_duration > 0:
                        existing_task["duration"] += additional_duration
                        print(f"Updated '{existing_task['name']}' total duration: {existing_task['duration']} mins.\n")
                        return
                    print("Duration must be greater than zero.")
                except ValueError:
                    print("Invalid input. Please enter a valid positive whole number.")
        else:
            task_name = input("Please enter a new unique task name: ").strip()
            if not task_name:
                return

    # Prompt for duration of new task
    while True:
        duration_input = input(f"Enter duration in minutes for '{task_name}': ").strip()
        try:
            duration = int(duration_input)
            if duration > 0:
                break
            print("Duration must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid positive whole number.")

    tasks.append({"name": task_name, "duration": duration})
    print(f"Added task '{task_name}' ({duration} mins).\n")


def remove_task(tasks):
    """Allows selecting and removing a task by its displayed list number."""
    if not tasks:
        print("\nNo tasks to remove.\n")
        return

    print("\nCurrent Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"  {idx}. {task['name']:<20} : {task['duration']} mins")

    while True:
        choice = input("\nEnter task number to remove (or 'c' to cancel): ").strip()
        if choice.lower() == "c":
            print("Removal canceled.\n")
            return

        try:
            task_num = int(choice)
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed task '{removed['name']}' ({removed['duration']} mins).\n")
                return
            else:
                print(f"Please enter a number between 1 and {len(tasks)}.")
        except ValueError:
            print("Invalid selection. Please enter a valid task number.")


def display_summary(tasks):
    """Displays task list and summary statistics."""
    if not tasks:
        print("\nNo tasks to display.")
        return

    total_minutes = sum(task["duration"] for task in tasks)
    longest_task = max(tasks, key=lambda task: task["duration"])

    print("\n" + "=" * 35)
    print("         SUMMARY REPORT          ")
    print("=" * 35)

    print("Entered Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"  {idx}. {task['name']:<20} : {task['duration']} mins")

    print("-" * 35)
    print(f"Total tasks entered : {len(tasks)}")
    print(f"Total time spent    : {total_minutes} minutes")
    print(
        f"Longest task        : {longest_task['name']} ({longest_task['duration']} minutes)"
    )
    print("=" * 35 + "\n")


def main():
    tasks = []

    while True:
        print("--- Task Duration Tracker ---")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. View Summary Report")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            display_summary(tasks)
        elif choice == "4":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select options 1 through 4.\n")


if __name__ == "__main__":
    main()