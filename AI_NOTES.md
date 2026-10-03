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



## Improvement 3 Feature Description
Feature Duplicate Task Duration Aggregation
Behavior If an existing task name is entered again (exact match after trimming), the program automatically adds the new minutes to the previous task entry rather than creating a duplicate row.

Make Improvement: reject blank durations, nonnumeric values, zero, and negative values without crashing.

Here is the improved version of your code.

Your existing validation loop (while True with duration_input.isdigit() and int(duration_input) > 0) already catches blank strings, letters/symbols, zero, and negative numbers without crashing. To make it more robust against edge cases (such as positive signed integers like +15 or floating-point numbers like 15.5 causing false negatives), we can replace .isdigit() with a try-except block parsing float() or int().

Improved Code
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

        # Validate that duration is numeric, non-blank, and strictly positive (> 0)
        while True:
            duration_input = input(
                f"Enter duration in minutes for '{task_name}': "
            ).strip()

            try:
                # Convert input to int (or float if decimals are allowed)
                duration = int(duration_input)
                
                if duration > 0:
                    break
                else:
                    print("Duration must be greater than zero.")
            except ValueError:
                # Triggers on blank inputs, non-numeric strings, or floats
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
Key Enhancements
Explicit Error Messages: Using a try-except ValueError allows you to differentiate between a non-numeric string (e.g., "" or "abc") and a number that is zero or negative (e.g., 0 or -5), allowing for clear, specific error prompts.

Crash Prevention: Bad types cannot raise a unhandled ValueError when cast to numeric types.

Rejection Rules Met:

Blank input (""): Caught by ValueError during parsing.

Non-numeric ("ten"): Caught by ValueError during parsing.

Zero (0): Rejects via duration > 0 condition.

Negative values (-10): Rejects via duration > 0 condition.


AI Tests

Normal Input
--- Task Duration Tracker ---
Enter a task name, then its duration in minutes.
Press Enter on a blank task name when you are finished.

Enter task name: Math 
Enter duration in minutes for 'Math': 30

Enter task name: Reading
Enter duration in minutes for 'Reading': 45

Enter task name: 

===================================
          SUMMARY REPORT          
===================================
Entered Tasks:
  1. Math                 : 30 mins
  2. Reading              : 45 mins
-----------------------------------
Total tasks entered : 2
Total time spent    : 75 minutes
Longest task        : Reading (45 minutes)
===================================

Boundary Input
--- Task Duration Tracker ---
Enter a task name, then its duration in minutes.
Press Enter on a blank task name when you are finished.

Enter task name: minute
Enter duration in minutes for 'minute': 1

Enter task name: 

===================================
          SUMMARY REPORT          
===================================
Entered Tasks:
  1. minute               : 1 mins
-----------------------------------
Total tasks entered : 1
Total time spent    : 1 minutes
Longest task        : minute (1 minutes)
===================================

Invalid Input
--- Task Duration Tracker ---
Enter a task name, then its duration in minutes.
Press Enter on a blank task name when you are finished.

Enter task name: Help
Enter duration in minutes for 'Help': -2
Duration must be greater than zero.
Enter duration in minutes for 'Help': 0 
Duration must be greater than zero.
Enter duration in minutes for 'Help': ds
Invalid input. Please enter a valid positive whole number (e.g., 15, 30).
Enter duration in minutes for 'Help': 