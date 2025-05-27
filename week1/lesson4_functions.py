# lesson4_functions.py

def greet_user(name):
    print(f"Hello, {name}!")

def is_eligible_to_vote(age):
    return age >= 18

def calculate_area(length, width):
    return length * width

# Using the functions
greet_user("Digbijoy")

age = 20
if is_eligible_to_vote(age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

area = calculate_area(5, 3)
print(f"The area of the rectangle is {area}")            



##"""If anyones is by anychance reading this to learn pythong , ur at wrong place mate these are codes i wrote as exercise after learning ##from w3schools and doing their exersices"""
