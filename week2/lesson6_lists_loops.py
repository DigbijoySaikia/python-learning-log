print("Let's make a list of your friends.")
friends = []

while True:
    name = input("Type friend's name (or type 'no friends left' to stop): ")
    if name.lower() == "no friends left":
        break
    friends.append(name)


print("\nYou have", len(friends), "friends.")
print("Here's your friends list:")
for f in friends:
    print("-", f)

# check if someone is your friend
check_name = input("\nType a name to check if they are your friend: ")
if check_name in friends:
    print(check_name, "is in your friends list.")
else:
    print(check_name, "is not your friend.")




