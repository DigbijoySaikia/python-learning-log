

# My favorite foods, fixed list — I can't change it later
fav_foods = ("pizza", "burger", "momos", "biryani")

print("My top 4 favorite foods are:")
for food in fav_foods:
    print("-", food)

# If I try to change a food here, Python will complain
# because tuples don’t let you change items once set
# fav_foods[0] = "pasta"



# Time to collect hobbies from the user, but use a set
# Sets don’t allow duplicates, so it keeps things unique
print("\nNow type some hobbies. Type 'done' when finished.")
hobbies = set()

while True:
    hobby = input("Type a hobby: ")
    if hobby.lower() == "done":
        break
    hobbies.add(hobby)

print("\nHere are your hobbies:")
for h in hobbies:
    print("-", h)

# Let's add "reading" twice to show duplicates don’t get saved twice
hobbies.add("reading")
hobbies.add("reading")  # second one is ignored

print("\nAfter adding 'reading' twice:")
for h in hobbies:
    print("-", h)
