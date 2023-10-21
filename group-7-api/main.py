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
    books_purchased = 0
    total_price = 0

    while True: # While loop for multiple book purchases
        book_id_to_buy = input("Enter the Book ID you want to buy: ").strip()
        branch_id = input('''Enter the Branch ID where you want to buy the book: 
            1 = Sutton
            2 = Glasgow
            3 = Edinburgh
            ''').strip()

        # Check availability and stock
        availability_result, stock = db_utils.check_book_availability(book_id_to_buy, branch_id)

        if availability_result is not None:
            if availability_result:
                print(f"The book is available in this branch, and there are {stock} copies in stock.")
                book_price = db_utils.get_book_price(book_id_to_buy)
                books_purchased += 1 # Increase books purchased by 1
                total_price += book_price # Add book price to total price
                print(f"Total Price So Far: £{total_price:.2f}")
            else:
                print("The book is not currently available in this branch. Please select a different book.")
        else:
            print("Book not found in the specified branch.")

        # If 3 or more books purchased, apply 10% discount
        if books_purchased >= 3:
            discount = total_price*0.1
            total_price -= discount # Discounted price
            print("Congratulations! You've received a 10% discount!")
            print(f"New Total Price: £{total_price:.2f}")

        # Allow user to purchase another book
        buy_option = input("Do you want to purchase another book: ").strip().lower()
        if buy_option != "y":
            print(f"Basket contains {books_purchased} books.")
            print(f"Total Price: £{total_price:.2f}")
            print("Returning to main menu")
            return


def explore_genres():
    print("Exploring genres...")
 # Retrieve a list of all available genres from the database
    genres = db_utils.get_genres()

    if genres:
        print("\nAvailable Genres:")
        for genre_name in genres:
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
    matching_books = db_utils.get_author_records()

    if matching_books:
        print("\nBooks by the selected author:")
        for book in matching_books:
            book_id, title, genre, price, stock = book
            print(f"Book ID: {book_id}, Title: {title}, Genre: {genre}, Price: £{price:.2f}, Stock: {stock}")
    else:
        print(f"No books found by '{author_search}' author.")


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


