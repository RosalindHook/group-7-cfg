import requests
import json
from banner import banner
import db_utils


def browse_books():
    result = requests.get('http://127.0.0.1:5003/books')
    if result.status_code == 200:
        books = result.json()
        if books:
            print("\nAvailable Books:")
            print(f"{'Book ID':<10}{'Title':<40}{'Author':<30}{'Price':<10}")
            print("-" * 90)
            for book in books:
                book_id = book["BookID"]
                title = book["Title"]
                author = book["Author"]
                price = book["Price"]
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
    else:
        print("Failed to retrieve book data.")


def buy_book():
    books_purchased = 0
    total_price = 0

    while True: # While loop for multiple book purchases
        book_id_to_buy = input("Enter the Book ID you want to buy: ").strip()
        branch_id = input('''Enter the Branch ID where you want to buy the book: 
            1 = Sutton
            2 = Glasgow
            3 = London
            4 = Edinburgh
            ''').strip()

        # Check availability and stock
        availability_result, stock = db_utils.check_book_availability(book_id_to_buy, branch_id)

        if availability_result:
            print(f"The book is available in this branch, and there are {stock} copies in stock.")
            book_price = db_utils.get_book_price(book_id_to_buy)
            books_purchased += 1  # Increase books purchased by 1
            total_price += book_price  # Add book price to total price

            # Send a POST request to the server to add a book to the basket
            response = requests.post('http://127.0.0.1:5003/buy-book', json={
                "book_id": book_id_to_buy,
                "branch_id": branch_id
            })

            if response.status_code == 200:
                print("Book added to basket successfully.")
                print(f"Total price so far: £{total_price:.2f}")
            else:
                print("Failed to add book to basket.")
                print(f"server response: {response.text}")
        else:
            print("The book is not currently available in this branch.")

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
            book_id, title, author, price = book
            print(f"Book ID: {book_id}, Title: {title}, Author: {author}, Price: £{price:.2f}")
    else:
        print(f"No books found for the '{genre_search}' genre.")


def explore_authors():
    print("Exploring authors...")
    # Retrieve a list of authors from the database
    authors = db_utils.get_authors_records()

    if authors:
        print("\nAuthors available:")
        for author in authors:
            print(author[0])

        selected_author = input("\nEnter the Author's name (full or partial) to explore books by that author: ").strip()

        # Retrieve books by the selected author
        matching_books = db_utils.get_books_by_author_name(selected_author)

        # Retrieve books based on the entered author's name

        if matching_books:
            print(f"\nBooks available from {selected_author}:")
            for book in matching_books:
                book_id, title, author, price = book
                print(f"Book ID: {book_id}, Title: {title}, Author: {author}, Price: £{price:.2f}")
        else:
            print(f"No books found by {selected_author}.")
    else:
        print("No authors found.")


def random_bonus():
    result = requests.get('http://127.0.0.1:5003/bonus')
    if result.status_code == 200:
        books = result.json()
        if books:
            print("\n Congratulations:")
            print(f"{'Book ID':<10}{'Title':<40}{'Author':<30}{'Price':<10}")
            print("-" * 90)
            for book in books:
                book_id = book["BookID"]
                title = book["Title"]
                author = book["Author"]
                price = book["Price"]
                print(f"{book_id:<10}{title:<40}{author:<30}£{price:.2f}")

            print("-" * 90)

            bonus_option = input("\n Choose a book and type the ID: ").strip().lower()
            found = False
            for book in books:
                if bonus_option == str(book["BookID"]):  # Convert book ID to a string for comparison
                    print(f'You can buy it for £{book["Price"] / 2:.2f}')
                    found = True
                    break

            if not found:
                print("Invalid book ID. Please type the correct ID.")


# function to run menu with options
def run():
    print(banner)
    print("Welcome to the Code Queens' Bookshop!\n")
    while True:
        menu_choice = input('''\nPlease select from the following options:
            1 - Browse books
            2 - Explore genres
            3 - Explore authors
            4 - Get bonus
            E - Exit the bookshop
            ''').lower()

        if menu_choice == "1":
            browse_books()  # Call a function to browse books
        elif menu_choice == "2":
            explore_genres()  # Call a function to explore genres
        elif menu_choice == "3":
            explore_authors()
        elif menu_choice == "4":
            random_bonus()  # for getting bonus
        elif menu_choice == "e":
            print("Exiting the book shop - goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == '__main__':

    run()


