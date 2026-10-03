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

        # Validate that duration is numeric, non-blank, and strictly positive (> 0)
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
    print("\n" + "=" * 35)
    print("          SUMMARY REPORT          ")
    print("=" * 35)
    
    # Task Breakdown
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