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
