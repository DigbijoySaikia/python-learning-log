# lesson3_loops.py

#  list of books
books = ["Python Basics", "Deep Learning", "Clean Code"]

for book in books:
    print(f"One of my favorite books: {book}")

# Using range to repeat something 5 times
for i in range(1, 6):
    print(f"Looping number: {i}")

# While loop: countdown from 5 to 1
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1

print("Lift off!")
