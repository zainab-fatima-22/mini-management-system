from user_module import add_user, view_users
from inventory_module import add_item, view_items
from transaction_module import borrow_item, return_item
from report_module import show_report

def menu():
    while True:
        print("\n===== SYSTEM MENU =====")
        print("1. Add User")
        print("2. View Users")
        print("3. Add Item")
        print("4. View Items")
        print("5. Borrow Item")
        print("6. Return Item")
        print("7. Show Report")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_user(input("ID: "), input("Name: "))

        elif choice == "2":
            view_users()

        elif choice == "3":
            add_item(input("ID: "), input("Name: "))

        elif choice == "4":
            view_items()

        elif choice == "5":
            borrow_item(input("Item ID: "))

        elif choice == "6":
            return_item(input("Item ID: "))

        elif choice == "7":
            show_report()

        elif choice == "0":
            print("Exiting system...")
            break

        else:
            print("Invalid choice")

menu()
