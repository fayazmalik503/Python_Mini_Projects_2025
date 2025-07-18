# To-Do List Application in Python

# Importing required modules
import os  # For file operations (we'll use this to save tasks)

"""
Learning Point: 
- Comments start with # for single line or triple quotes for multi-line
- Importing modules using 'import' statement
"""

# Initialize an empty list to store tasks
tasks = []

"""
Learning Point:
- Variables and data types (list in this case)
- We'll use this list to store our tasks
"""

def display_menu():
    """Display the main menu of the application"""
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Save Tasks to File")
    print("6. Load Tasks from File")
    print("7. Exit")

"""
Learning Point:
- Function definition using 'def'
- Docstrings (triple-quoted strings) for function documentation
- Printing multiple lines
"""

def add_task():
    """Add a new task to the list"""
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

"""
Learning Point:
- Taking user input with input()
- Appending to a list with append()
- Using f-strings for formatted strings
- Dictionary data structure to store task details
"""

def view_tasks():
    """Display all tasks with their completion status"""
    if not tasks:
        print("No tasks in the list!")
    else:
        print("\nTask List:")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['task']}")

"""
Learning Point:
- Checking if list is empty
- enumerate() to get index while looping
- Ternary operator for conditional status
- Accessing dictionary values
"""

def mark_complete():
    """Mark a task as completed"""
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to mark as complete: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num-1]["completed"] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

"""
Learning Point:
- Error handling with try-except
- Type conversion with int()
- List indexing
- Input validation
"""

def delete_task():
    """Delete a task from the list"""
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num-1)
                print(f"Task '{removed_task['task']}' deleted!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

"""
Learning Point:
- Removing items from list with pop()
- Similar validation pattern as mark_complete()
"""

def save_to_file():
    """Save tasks to a text file"""
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']},{task['completed']}\n")
    print("Tasks saved to tasks.txt")

"""
Learning Point:
- File operations with 'with' statement (automatically closes file)
- Writing to files
- String formatting for storage
"""

def load_from_file():
    """Load tasks from a text file"""
    if os.path.exists("tasks.txt"):
        tasks.clear()
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                tasks.append({
                    "task": task_data[0],
                    "completed": task_data[1] == "True"
                })
        print("Tasks loaded from tasks.txt")
        view_tasks()
    else:
        print("No saved tasks found!")

"""
Learning Point:
- Checking if file exists
- Reading from files
- String manipulation (strip, split)
- Type conversion (string to boolean)
"""

# Main application loop
def main():
    """Main function to run the application"""
    print("Welcome to the To-Do List App!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_to_file()
        elif choice == "6":
            load_from_file()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-7.")

"""
Learning Point:
- While loop for continuous program execution
- if-elif-else conditional statements
- Calling other functions
- Program exit with break
"""

# This ensures the main() function runs only when the script is executed directly
if __name__ == "__main__":
    main()

"""
Learning Point:
- Python's special __name__ variable
- This is a common Python idiom to make files both importable and executable
"""