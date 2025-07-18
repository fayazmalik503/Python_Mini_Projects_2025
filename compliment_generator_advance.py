import random

# Step 1: Compliment list (10 total — 5 purani, 5 nayi)
compliments = [
    "You're doing great!",
    "You're a fast learner!",
    "Python loves you!",
    "You're going to be an amazing developer!",
    "You have a brilliant mind!",
    # Tumhari 5 khud ki lines
    "You think like a real programmer!",
    "Your logic is getting stronger every day!",
    "You’re shining brighter with every line of code!",
    "Your curiosity makes you unstoppable!",
    "You have the power to build amazing apps!"
]

# Step 2: Naam lo
name = input("Enter your name: ")

# Step 3: Pehla compliment
compliment1 = random.choice(compliments)
print("Hi " + name + "! " + compliment1)

# Step 4: Dusra compliment
compliment2 = random.choice(compliments)
print("Also, " + compliment2)

# Step 5: User se poochhna
another = input("Do you want another compliment? (yes/no): ")

# Step 6: Agar user ne yes bola
if another.lower() == "yes":   # Agar user ne "YES", "Yes", "YeS" ya kuch bhi likha ho — sabko chhoti letters mein convert karta hai.
    compliment3 = random.choice(compliments)
    print("Here you go, " + name + ": " + compliment3)
else:
    print("Okay, have a great day " + name + "! 😊")