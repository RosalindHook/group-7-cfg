# import requests   commented as not yet used
# import json    commented out as not yet used
from banner import banner
import db_utils


def browse_books():
    books = db_utils.get_all_books()
    if books:
        print("\nAvailable Books:")
        print(f"{'Book ID':<10}{'Title':<40}{'Author':<30}{'Price':<10}")
        print("-" * 90)
        for book in books:
            book_id, title, author, price = book
            print(f"{book_id:<10}{title:<40}{author:<30}£{price:.2f}")
        print("-" * 90)

        buy_option = input("\nWould you like to buy a book? (Y/N): ").strip().lower()
        if buy_option == "y":
            buy_book()
        elif buy_option == "n":
            print("Returning to the main menu.")
        else:
            print("Invalid choice. Returning to the main menu.")
    else:
        print("No books found in stock.")


def buy_book():
    book_id_to_buy = input("Enter the Book ID you want to buy: ").strip()
    branch_id = input('''Enter the Branch ID where you want to buy the book: 
    1 = Sutton
    2 = Glasgow
    3 = Edinburgh
    ''').strip()

    availability_result, stock = db_utils.check_book_availability(book_id_to_buy, branch_id)

    if availability_result is not None:
        # check if the availability result is a list with data
        if availability_result:
            print(f"The book is available in this branch, and there are {stock} copies in stock.")
        else:
            print("The book is not currently available in this branch. Please select a different book.")
    else:
        print("Book not found in the specified branch.")

###############################################################
def buy_book():
    books_purchased = 0
    total_price = 0

    while True: # While loop for multiple book purchases
        book_id_to_buy = input("Enter the Book ID you want to buy: ").strip()
        branch_id = input('''Enter the Branch ID where you want to buy the book: 
            1 = Sutton
            2 = Glasgow
            3 = Edinburgh
            ''').strip()

        # Check avaialbility and stock
        availability_result, stock = db_utils.check_book_availability(book_id_to_buy, branch_id)

  
###############################################################
def explore_genres():
    print("Exploring genres...")
 # Retrieve a list of all available genres from the database
    genres = db_utils.get_all_genres()

    if genres:
        print("\nAvailable Genres:")
        for genre_id, genre_name in genres:
            print(f"{genre_name}")
    else:
        print("No genres found.")

    genre_search = input("\nEnter the genre you want to explore (full or partial name): ").strip()

    # Retrieve books based on the entered genre name
    matching_books = db_utils.get_books_by_genre_name(genre_search)

    if matching_books:
        print("\nBooks in the selected genre:")
        for book in matching_books:
            book_id, title, author, price, stock = book  # Added 'stock' to the unpacking
            print(f"Book ID: {book_id}, Title: {title}, Author: {author}, Price: £{price:.2f}, Stock: {stock}")
    else:
        print(f"No books found for the '{genre_search}' genre.")


def explore_authors():
    print("Exploring authors")

    author_search = input("\nEnter the author you want to explore: ").strip()
    authors = db_utils.search_authors_by_name(author_search)

    if authors:
        print("\nAuthors available:")
        for author_id, first_name, last_name in authors:
            # Print a list of available authors
            print(f"{author_id}: {first_name} {last_name}")

        selected_author = input("\nEnter the Author's name to explore books by that author: ").strip()

        # Retrieve books by the selected author using the author's name
        books_by_author = db_utils.get_books_by_author_name(selected_author)

        if books_by_author:
            print(f"\nBooks available from {selected_author}:")
            for book_id, title, genre, price, stock in books_by_author:
                # Print a list of books by the selected author
                print(f"Book ID: {book_id}, Title: {title}, Genre: {genre}, Price: £{price:.2f}, Stock: {stock}")
        else:
            print(f"No books found by {selected_author}.")
    else:
        print("No authors found.")


def check_stock_availability():
    print("Checking stock availability...")


# function to run menu with options
def run():
    print(banner)
    print("Welcome to the Code Queens' Bookshop!\n")
    while True:
        menu_choice = input('''\nPlease select from the following options:
            1 - Browse books
            2 - Explore genres
            3 - Explore authors
            4 - Check stock availability
            E - Exit the bookshop
            ''').lower()

        if menu_choice == "1":
            browse_books()  # Call a function to browse books
        elif menu_choice == "2":
            explore_genres()  # Call a function to explore genres
        elif menu_choice == "3":
            explore_authors()
        elif menu_choice == "4":
            check_stock_availability()  # Call a function to check stock availability
        elif menu_choice == "e":
            print("Exiting the book shop - goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == '__main__':

    run()
