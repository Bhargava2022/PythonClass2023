def contains_invalid_chars(phone):
    """Check if the phone number contains any invalid characters."""
    for char in phone:
        if char not in '0123456789-()':
            return True
    return False

def is_correct_length(phone):
    """Check if the phone number is of the correct length (10 numbers)."""
    digits_only = ''.join(filter(str.isdigit, phone))
    return len(digits_only) == 10

def format_phone(phone):
    """Format the phone number in the desired (xxx)xxx-xxxx format."""
    digits_only = ''.join(filter(str.isdigit, phone))
    return f"({digits_only[:3]}){digits_only[3:6]}-{digits_only[6:]}"

def main():
    while True:
        phone = input("Please enter a phone number (or 'q' to quit): ")

        if phone == 'q':
            break

        # 1. Check for invalid characters
        if contains_invalid_chars(phone):
            print("The phone number contains invalid characters. Please try again.")
            continue

        # 2. Check for length
        if not is_correct_length(phone):
            print("The phone number should have exactly 10 digits. Please try again.")
            continue

        # 3. Format the phone number
        formatted_phone = format_phone(phone)
        print(f"Formatted Phone Number: {formatted_phone}")

if __name__ == "__main__":
    main()
