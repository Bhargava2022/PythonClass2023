import csv
import re

def phone_validation(phone_number):
    # A simple example to validate and standardize U.S. phone numbers
    match = re.match(r'^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$', phone_number)
    if match:
        return "({}) {}-{}".format(*match.groups())
    else:
        return None

def enter_new_contact():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    phone_number = input("Enter Phone Number: ")
    standardized_phone = phone_validation(phone_number)
    if standardized_phone:
        with open('contacts.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([first_name, last_name, standardized_phone])
        print("Contact saved!")
    else:
        print("Invalid phone number. Contact not saved.")

def view_all_contacts():
    try:
        with open('contacts.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print("No contacts found.")

def main():
    while True:
        print("\nMenu:")
        print("1. Enter New Contact")
        print("2. View all Contacts")
        print("3. Quit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            enter_new_contact()
        elif choice == '2':
            view_all_contacts()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose from the options provided.")

if __name__ == "__main__":
    main()
