## DAY 1

### starting by storing some information about a person
name = "Digbijoy"          ##  i learnt a bit of pyton so i can make it take inputs but lets stick to the book##
age = 25                   # :3 if someone wants to do that though its like  name = input("what is your name :")
height_meters = 1.75
is_student = True  # True means yes False  means no

#summarizing about the person using an f-string to make it easy to read
summary = f"{name} is {age} years old, {height_meters} meters tall, and student status is {is_student}."
print(summary)

# Sometimes it's useful to know what kind of data we're working with
print(f"'age' is of type: {type(age)}")
print(f"'height_meters' is of type: {type(height_meters)}")

#just something to pass time 
next_year_age = age + 1
print(f"Next year, {name} will be {next_year_age} years old.")

# Just for fun converting height from meters to centimeters
height_cm = height_meters * 100
print(f"That means {name} is {height_cm} centimeters tall.")                            




##    WILL SOMEONE EVEN READ THIS ?     ### 
