"""🟢 Jo seekhogay:

Multiple input()

int() conversion

Variables aur math

String + number ko combine kaise karte hain"""

#koi bhi name likhny k lye
name = input("Enter your name: ")

#current age lene k lye
age = int(input("Enter you current age: "))

#kitny sal ka future age dekhna hy?
years = int(input("How many years into the future do you want to see your age?"))

#future age calculation krny k lye
future_age = age + years

# print result
print("Hi " + name + "! in " + " years, you will be " + str(future_age) +  "years old.")