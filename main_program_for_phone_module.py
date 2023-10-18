import phone_module

def main():
    while True:
        phone = input("Please enter a phone number (or 'q' to quit): ")

        if phone == 'q':
            break

        # 1. Check for invalid characters
        if phone_module.contains_invalid_chars(phone):
            print("The phone number contains invalid characters. Please try again.")
            continue

        # 2. Check for length
        if not phone_module.is_correct_length(phone):
            print("The phone number should have exactly 10 digits. Please try again.")
            continue

        # 3. Format the phone number
        formatted_phone = phone_module.format_phone(phone)
        print(f"Formatted Phone Number: {formatted_phone}")

if __name__ == "__main__":
    main()
