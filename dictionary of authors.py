# Defining a dictionary where each key is an author's name and each value is a list of books they have written
authors_books = {
    "Jane Austen": ["Pride and Prejudice", "Sense and Sensibility"],
    "Ernest Hemingway": ["The Old Man and the Sea", "A Farewell to Arms"],
    "George Orwell": ["1984", "Animal Farm"]
}

# Getting user input for author's name
author_name = input("Enter the name of an author: ")

# Checking if the author exists in the dictionary and printing the list of books they wrote
if author_name in authors_books:
    print(f"Books written by {author_name}:")
    for book in authors_books[author_name]:
        print(f"- {book}")
else:
    print(f"Sorry, {author_name} is not in our database.")
