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

def display_name():
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

def display_name():
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

print(add_task())
"""
Learning Point:
- Taking user input with input()
- Appending to a list with append()
- Using f-strings for formatted strings
- Dictionary data structure to store task details
"""