from contact_manager import add_contact, view_contacts, remove_contact, search_contact
from file_handler import save_to_file, load_from_file
from validation import validate_name, validate_email, validate_phone

def main():
    global contacts
    contacts = load_from_file()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                name = input("Enter Name: ")
                validate_name(name)
                email = input("Enter Email: ")
                validate_email(email)
                phone = input("Enter Phone: ")
                validate_phone(phone)
                address = input("Enter Address: ")
                print(add_contact(name, email, phone, address))
                save_to_file(contacts)
            except ValueError as e:
                print(e)

        elif choice == "2":
            print(view_contacts())

        elif choice == "3":
            phone = input("Enter Phone of Contact to Remove: ")
            print(remove_contact(phone))
            save_to_file(contacts)

        elif choice == "4":
            query = input("Enter search query: ")
            print(search_contact(query))

        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
