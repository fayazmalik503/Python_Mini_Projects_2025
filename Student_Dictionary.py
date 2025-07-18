# Step 1: User se data lena
name = input("Enter student name: ")
age = int(input("Enter student age: "))
grade = input("Enter student grade: ")
city = input("Enter student city: ")

# Step 2: Data ko dictionary mein store karna
student = {
    "name": name,
    "age": age,
    "grade": grade,
    "city": city
}

# Step 3: Show the stored data
print("\n--- Student Record Stored ---")
print("Student Dictionary:", student)        

# Step 4: Individual fields print karna (proof of access)
print("\nAccessing individual values:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Grade:", student["grade"])
print("City:", student["city"])