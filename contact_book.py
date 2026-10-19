
# Contact Book Management System

contacts = []


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if not name or not phone:
        print("Name and phone number are required.")
        return

    for contact in contacts:
        if contact["phone"] == phone:
            print("This phone number already exists.")
            return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")

    for number, contact in enumerate(contacts, start=1):
        print(f"\nContact {number}")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"] or "Not provided")


def search_contact():
    name = input("Enter name to search: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("\nContact found!")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"] or "Not provided")
            return

    print("Contact not found.")


def delete_contact():
    phone = input("Enter phone number to delete: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


def main():
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Contact Book closed.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
