def get_name_and_age():
    #docstring
    """
    Prompt the user for their name and age.
    
    Exception Handling:
    - Ensures that the age provided is a valid integer.
    - Checks that the age isn't negative.
    
    Returns:
        tuple: A tuple containing name (str) and age (int).
    """
    while True:
        # Prompting user for name input.
        name = input("Please enter your name: ")

        # Attempt to gather and validate user's age.
        try:
            age = int(input("Please enter your age: "))
            
            # Age validation: Ensure it's non-negative.
            if age < 0:
                raise ValueError("Age cannot be negative.")
            
            # If all checks pass, return the name and age.
            return name, age
        
        # Handle potential input errors, guiding user for correct input.
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid age.")


def count_letters(name):
    #docstring
    """
    Count the number of letters in the provided name.

    Args:
    - name (str): The name whose letters are to be counted.

    Returns:
    - int: The number of letters in the name.
    """
    # Calculate and return the total letters in the provided name.
    return len(name)


def can_vote(age):
    #docstring
    """
    Check if the person is old enough to vote.

    Args:
    - age (int): The age of the person.

    Returns:
    - bool: True if the person is 18 or older, otherwise False.
    """
    # Determine voting eligibility based on age.
    return age >= 18


def is_even(age):
    #docstring
    """
    Check if the age is even.

    Args:
    - age (int): The age of the person.

    Returns:
    - bool: True if the age is even, otherwise False.
    """
    # Check for evenness using the modulo operator.
    return age % 2 == 0


def main():
    # Initiate interaction with the user.
    name, age = get_name_and_age()
    
    # Display insights about the user's name.
    print(f"There are {count_letters(name)} letters in the name '{name}'.")

    # Provide feedback on voting eligibility.
    if can_vote(age):
        print("You are old enough to vote!")
    else:
        print("You are not old enough to vote.")
    
    # Inform user if their age is even or odd.
    if is_even(age):
        print("Your age is even.")
    else:
        print("Your age is odd.")


# Ensure the main function runs when the script is executed directly.
if __name__ == "__main__":
    main()
