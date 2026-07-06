import json
contacts = []

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    if not name or not phone or not email:
        print("Error: All fields (name, phone, email) are required!")
        return

    details = {"name": name, "phone": phone, "email": email}

    contacts.append(details)
    save_contacts()
    print("Contact added successfully!")

def view_contacts():
    for person in contacts:
        print("Name: ", person["name"], "Phone: ", person["phone"], "Email: ", person["email"])


def search_contact():
    name = input("Enter the name you want to search: ").strip()
    for person in contacts:
        if person["name"].lower() == name.lower():
            print("Name: ", person["name"], "Phone: ", person["phone"], "Email: ", person["email"])
            return
    print("Contact not found")

def delete_contact():
    name = input("Enter the name you want to delete: ")
    for person in contacts:
        if person["name"] == name.strip().lower():
            contacts.remove(person)
            save_contacts()
            print("Contact Deleted")
            return
    print("Contact not found")

def save_contacts():
    try:
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=2)
    except IOError as e:
        print(f"Error saving contacts: {e}")

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    except json.JSONDecodeError:
        print("Warning: Corrupted contacts file. Starting fresh.")
        contacts = []

def main():
    load_contacts()
    while True:
        print("\n1. Add Contact")
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
            print("Goodbye!")
            break
        else:
            print("Enter a valid number!")

if __name__ == "__main__":
    main()