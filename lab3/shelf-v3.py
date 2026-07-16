# Shelf v0.3 — a shelf that holds many books

shelf = []  # list for the book

while 1:
    print("--- Shelf ---")
    
    user_input = input("[1] Add a book\n[2] List all books\n[3] Search for a book\n[4] Remove a book\n[Q] Quit\nChose: ")

    if user_input == '1':   # add a book
        title = input("Please enter book title >> ")
        if title in shelf:
            print(f"{title} already on the shelf!")
        else:
            shelf.append(title)
            print(f"You have entered {title}")
    elif user_input == '2': # list all books
        if len(shelf) == 0:
            print("Shelf is empty")
        else:
            shelf = sorted(shelf)
            for index, title in enumerate(shelf, start=1):
                print(f"{index}. {title}")
    elif user_input == '3': # search a title
        title = input("Please enter book title you want to search >> ")
        if title in shelf:
            print(f"{title} already on the shelf!")
        else:
            a_input = input(f"{title} is not on the shelf!\nPress [1] if you want to add it to the shelf, press any other key to go gack to main menu >> ")
            if a_input == '1':
                shelf.append(title)
                print(f"You have added {title} to the shelf!") 
    elif user_input == '4': # remove a title
        title = input("Please enter book title you want to remove >> ")
        if title in shelf:
            shelf.remove(title)
            print(f"{title} is removed from the shelf")
        else:
            print(f"{title} is not on the shelf!")
    elif user_input.lower() == 'q':
        break
    else:
        print("Not part of the option, please input again.")