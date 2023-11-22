#Contact Book

# Initialize an empty dictionary to store contacts
contacts = {}

# Function to view the contact list
def view_contacts():
    print("---------------------")
    print("     CONTACT LIST")
    print("---------------------")
    for index, (name, phone) in enumerate(contacts.items(), start=1):
        print(f"{index}. {name} | {phone}")
    print("---------------------")

# Function to add a new contact
def add_contact():
    print("---------------------")
    print("     ADD CONTACT")
    print("---------------------")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print("\nContact added successfully!\n")

# Function to search for a contact
def search_contact():
    print("---------------------")
    print("    SEARCH CONTACT")
    print("---------------------")
    query = input("Enter Name or Phone Number: ")
    
    # Filter contacts based on the search query
    results = {name: contact['Phone'] for name, contact in contacts.items() if query.lower() in name.lower() or query in contact['Phone']}
    
    if results:
        print("\nSearch Results:")
        for index, (name, phone) in enumerate(results.items(), start=1):
            print(f"{index}. {name} | {phone}")
    else:
        print("\nNo matching contacts found.")
    print("---------------------")

# Function to update a contact
def update_contact():
    print("---------------------")
    print("    UPDATE CONTACT")
    print("---------------------")
    query = input("Enter the name or phone number of the contact to update: ")
    
    # Filter contacts based on the search query
    results = {name: contact for name, contact in contacts.items() if query.lower() in name.lower() or query in contact['Phone']}
    
    if results:
        print("\nContact Found:")
        for index, (name, contact) in enumerate(results.items(), start=1):
            print(f"{index}. {name} | {contact['Phone']}")
        
        choice = int(input("\nChoose the contact to update (1-" + str(len(results)) + "): "))
        selected_contact = list(results.keys())[choice - 1]
        
        # Get new details from the user
        new_name = input("Enter New Name: ")
        new_phone = input("Enter New Phone Number: ")
        new_email = input("Enter New Email: ")
        new_address = input("Enter New Address: ")
        
        # Update the contact
        contacts[new_name] = {'Phone': new_phone, 'Email': new_email, 'Address': new_address}
        del contacts[selected_contact]
        
        print("\nContact updated successfully!\n")
    else:
        print("\nNo matching contacts found.")
    print("---------------------")

# Function to delete a contact
def delete_contact():
    print("---------------------")
    print("    DELETE CONTACT")
    print("---------------------")
    query = input("Enter the name or phone number of the contact to delete: ")
    
    # Filter contacts based on the search query
    results = {name: contact['Phone'] for name, contact in contacts.items() if query.lower() in name.lower() or query in contact['Phone']}
    
    if results:
        print("\nContact Found:")
        for index, (name, phone) in enumerate(results.items(), start=1):
            print(f"{index}. {name} | {phone}")
        
        choice = int(input("\nChoose the contact to delete (1-" + str(len(results)) + "): "))
        selected_contact = list(results.keys())[choice - 1]
        
        # Delete the contact
        del contacts[selected_contact]
        
        print("\nContact deleted successfully!\n")
    else:
        print("\nNo matching contacts found.")
    print("---------------------")

# Main loop
while True:
    print("---------------------")
    print("   CONTACT MANAGER   ")
    print("---------------------")
    print("1. View Contact List")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("\nPlease enter your choice (1-6): ")
    
    if choice == '1':
        view_contacts()
    elif choice == '2':
        add_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting Contact Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
