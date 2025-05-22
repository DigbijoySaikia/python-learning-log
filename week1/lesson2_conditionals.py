# lesson2_conditionals.py

name = "Digbijoy"
age = 17

if age >= 18:
    print(f"{name} is eligible to apply for a driver's license.")
elif age == 17:
    print(f"{name} is almost there — just one more year!")
else:
    print(f"{name} is too young to drive.")
##----------------------------------------------------------------------------------------------------------------------
score = 82

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: D or below")
