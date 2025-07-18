# Step 1: User se naam lo
name = input("Enter your name: ")

# Step 2: User se age lo
age = input("Enter your current age: ")

# Step 3: String ko number mein convert karo
age = int(age)

# Step 4: 10 saal add karo
future_age = age + 10

# Step 5: Result print karo
print("Hi " + name + "! In 10 years, you will be " + str(future_age) + " years old.")