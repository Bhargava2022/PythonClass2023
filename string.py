# Get first and last name from the user
name_input = input("Enter your first and last name: ")

# Split the input into first and last name
first_name, last_name = name_input.split()

# Convert first name to all uppercase
first_name_upper = first_name.upper()

# Capitalize the first letter of the last name
last_name_cap = last_name.capitalize()

# Get the length of the last name
last_name_length = len(last_name)

# Print greetings and last name length
print(f"HELLO {first_name_upper}!")
print(f"There are {last_name_length} letters in your last name ({last_name_cap})")

# Get the state from the user and convert to uppercase
state = input("What state do you live in? (2 letter abbreviation) ").upper()

# Print the final output
print(f"Last name: {last_name_cap},    First name: {first_name.capitalize()},    Home state: {state}")
