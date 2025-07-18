#✅ Project: Multiple Students in a List of Dictionaries
#🧠 Goal:
#Har student ka data dictionary mein store karna, aur saare students ko ek list mein rakhna.

# Step 1: Empty list to store all students
students = []

# Step 2: Loop to take input for 3 students
for i in range(3):
    print(f"\nEnter data for student #{i+1}")
    name = input("Name: ")
    age = int(input("Age: "))
    grade = input("Grade: ")
    city = input("City: ")

    # Step 3: Dictionary banao for one student
    student = {
        "name": name,
        "age": age,
        "grade": grade,
        "city": city
    }

    # Step 4: List mein add karo
    students.append(student)

# Step 5: Show all students
print("\n--- All Student Records ---")
for s in students:
    print(f"{s['name']} from {s['city']} is in grade {s['grade']} and is {s['age']} years old.")