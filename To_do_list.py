# Step 1: Empty to-do list
todo_list = []

# Step 2: Loop for user menu
while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")
        if len(todo_list) == 0:
            print("No tasks yet.")
        else:
            for i, task in enumerate(todo_list):
                print(f"{i+1}. {task}")

    elif choice == "3":
        print("\nWhich task number to delete?")
        for i, task in enumerate(todo_list):
            print(f"{i+1}. {task}")
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(todo_list):
            removed = todo_list.pop(index - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please enter 1-4.")