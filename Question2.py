def add_book(library, new_book):

    if new_book in library:
        print("The book is already in the library.")
    else:
        library.append(new_book)
        print(f"Added '{new_book[0]}' by {new_book[1]} to the library.")


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

print(library)
