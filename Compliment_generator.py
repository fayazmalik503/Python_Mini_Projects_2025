"""User apna naam deta hai, aur program usko ek random positive compliment deta hai. 
   Ye project mazedaar bhi hai aur tumhe list + random seekhne ko milega."""

import random

# Step 1: Compliments ki list banao
compliments = ["You're doing great!",
    "You're a fast learner!",
    "Python loves you!",
    "You're going to be an amazing developer!",
    "You have a brilliant mind!"
    ]

# Step 2: User ka naam lo
name = input("Enter your name: ")

# Step 3: Random compliment choose karo
compliment = random.choice(compliments)


# Step 4: Show message
print("Hi " + name +  "! " + compliment)
