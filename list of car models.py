# List of car models
car_models = ["Accord", "Camry", "Civic", "Corolla", "Mustang", "Impreza"]

# Initialize an empty dictionary to store the car model and its manufacturer
car_dict = {}

# For each car model in the list, ask the user for its manufacturer
for model in car_models:
    manufacturer = input(f"Please enter the manufacturer of the {model}: ")
    car_dict[model] = manufacturer  # Add the model and manufacturer to the dictionary

# Iterate through the dictionary and print out the car model and its manufacturer
print("Here is the list of car models and their manufacturers:")
for model, manufacturer in car_dict.items():
    print(f"{model}: {manufacturer}")
