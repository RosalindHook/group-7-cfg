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


def explore_genres():
    print("Exploring genres...")

def explore_authors():
    print("Exploring authors")

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
