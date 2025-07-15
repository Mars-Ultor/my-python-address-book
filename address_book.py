contacts = {}


def add_contact(name, phone):
    """Add a new contact to the address book."""
    contacts[name] = phone
    print(f"Contact '{name}' added.")


def view_contacts():
    """Displays all contacts in the address book."""
    if not contacts:
        print("Address book is empty.")
    else:
        print("n--- Your Contacts ---")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
        print("----------------------\n")


def delete_contact(name):
    """Deletes a contact from the address boo."""
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")


def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("Address Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("enter name of contact to delete: ")
            delete_contact(name)
        elif choice == '4':
            print("Exiting the Address Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number betwwn 1 and 4.")


if __name__ == "__main__":
    main_menu()
