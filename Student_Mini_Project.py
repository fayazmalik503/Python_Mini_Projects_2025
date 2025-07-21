# Step 1: Student list (pehle se available data)
students = [
    {"name": "Ali", "age": 15, "grade": "10", "city": "Lahore"},
    {"name": "Sara", "age": 14, "grade": "9", "city": "Karachi"},
    {"name": "Ahmed", "age": 16, "grade": "11", "city": "Multan"}
]

# Step 2: User se naam lena
search_name = input("Enter the name of the student you want to search: ")

# Step 3: Flag banayein (mil gaya ya nahi)
found = False

# Step 4: Search through the list
for s in students:
    if s["name"].lower() == search_name.lower():
        print("\nStudent Found:")
        print("Name:", s["name"])
        print("Age:", s["age"])
        print("Grade:", s["grade"])
        print("City:", s["city"])
        found = True
        break  # Stop after finding the first match

# Step 5: Agar nahi mila to message
if not found:
    print("Student not found.")