# hour 1
print("📚 Welcome to the Book Recommender!")

def recommend_books(mood):
    # hour 3(edited to correct errors (at last i had to ask chat gpt to find my error )
    ## recs = recomended_books(mood) + user_books     output :NameError: name 'recomended_books' is not defined
    ### fix : it was a typing error i misspelled :{ 


    if mood == "happy":
        return ["The Alchemist", "Pride and Prejudice", "Eleanor Oliphant Is Completely Fine"]
    elif mood == "sad":
        return ["The Fault in Our Stars", "A Man Called Ove", "Norwegian Wood"]
    elif mood == "motivated":
        return ["Atomic Habits", "Deep Work", "Can't Hurt Me"]
    else:
        return []

def get_user_choice():
    print("\nWhat’s your current mood?")
    print("1. Happy")
    print("2. Sad")
    print("3. Motivated")
    print("4. Exit")

    choice = input("Choose a number: ")
    return choice

# hour 2
user_books = []

while True:
    option = get_user_choice()

    if option == "1":
        mood = "happy"
    elif option == "2":
        mood = "sad"
    elif option == "3":
        mood = "motivated"
    elif option == "4":
        break
    else:
        print("Invalid choice.")
        continue

    recs = recommend_books(mood) + user_books
    print("\nRecommended books for you:")
    for idx, book in enumerate(recs, 1):
        print(f"{idx}. {book}")

    # hour 3
    add = input("Want to add your own favorite book? (yes/no): ").lower()
    if add == "yes":
        new_book = input("Enter the book title: ")
        user_books.append(new_book)

print("\nThanks for using the recommender!")
