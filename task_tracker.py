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

        # Check for duplicate task names (case-insensitive)
        existing_task = next(
            (t for t in tasks if t["name"].lower() == task_name.lower()), None
        )

        if existing_task:
            print(f"Note: '{existing_task['name']}' already exists with {existing_task['duration']} mins.")
            action = input("Combine duration with existing task? [y/n]: ").strip().lower()

            if action == 'y':
                # Prompt for additional duration to add
                while True:
                    duration_input = input(
                        f"Enter additional minutes to add to '{existing_task['name']}': "
                    ).strip()

                    try:
                        additional_duration = int(duration_input)
                        if additional_duration > 0:
                            existing_task["duration"] += additional_duration
                            print(f"Updated '{existing_task['name']}' total duration: {existing_task['duration']} mins.\n")
                            break
                        else:
                            print("Duration must be greater than zero.")
                    except ValueError:
                        print("Invalid input. Please enter a valid positive whole number.")
                continue  # Skip to next task entry loop
            else:
                # If user doesn't want to combine, prompt for a new name
                task_name = input("Please enter a new unique task name: ").strip()
                if not task_name:
                    break

        # Validate duration for new task entries
        while True:
            duration_input = input(
                f"Enter duration in minutes for '{task_name}': "
            ).strip()

            try:
                duration = int(duration_input)
                if duration > 0:
                    break
                else:
                    print("Duration must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a valid positive whole number (e.g., 15, 30).")

        # Store new task
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
    print("\n" + "=" * 35)
    print("          SUMMARY REPORT          ")
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
    print("=" * 35)


if __name__ == "__main__":
    main()