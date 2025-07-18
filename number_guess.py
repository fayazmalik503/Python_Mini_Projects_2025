import random

# computer random number choose krta hy
secret_number = random.randint(1 , 10)

# Guess krwany ka message
print("Guess the numner between 1 to 10")

# jab tak sahi jawab na mily 
while True:
    guess = int(input("Enter you guess: "))
    if guess == secret_number:
        print("🎉 Correct! You guessed it!")
        break
    elif guess < secret_number:
        print("Too Low! Try again")
    else:
        print("Too high! try again")