def display_menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"{name} contact is added...!!!")

def view_contacts(contacts):
    if contacts:
        print("\nContacts:")
        for name, phone in contacts.items():
            print(f"Name: {name}\nPhone: {phone}")
    else:
        print("No contacts found.")

def update_contact(contacts):
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        contacts[name] = phone
        print(f"{name} contact updated.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} contact is deleted.")
    else:
        print("Contact not found.")

contacts = {}

while True:
    display_menu()
    c = input("Select an option  between 1-5: ")

    if c=='1':
        add_contact(contacts)
    elif c=='2':
        view_contacts(contacts)
    elif c=='3':
        update_contact(contacts)
    elif c=='4':
        delete_contact(contacts)
    elif c=='5':
        print("Exiting this is a the last choice")
        break
    else:
        print("Invalid choice Please select a valid option..!!!")
