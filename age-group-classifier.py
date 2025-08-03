# 🧮 Project Name: “Age Group Classifier”
"""🧠 Skills You Will Practice:
input()
if-elif-else conditions
Type conversion (int())
Real-world logic building
"""

# building

# 🎯 Project Goal:
"""User apni age enter karega, aur program batayega,
   wo kaunsi age group mein aata hai:
0-12 → Child
13-19 → Teenager
20-59 → Adult
60+ → Senior Citizen"""

print("👤 Welcome to the Age Group Classifier!")
# Step 1: Ask for user's name and age
name = input("What is your name: ")
age = input("Enter your age: ")

# Step 2: Convert age to number
if age.isdigit():
    age = int(age)

    #step 3: Classify based on age
    if age >=0 and age <=12: 
        print(f"{name}, you are a child.")
    elif age >= 13 and age <= 19:
        print(f"{name}, you are a teeneger")
    elif age >= 20 and age <= 59:
        print(f"{name}, you are an adult")
    elif age >= 60:
        print(f"{name}, you are a senior citizen")
    else:
        print("Hmmm ... that doesn't seems right")

else:
    print("Please insert the valid number for age")