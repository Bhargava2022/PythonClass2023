import random
import csv

# Define the functions
def calculate_annual_growth(current_balance, expected_rate):
    """ Calculate the annual growth based on the expected rate, 
        while allowing for a fluctuation of up to 20% """
    rate = expected_rate * (1 + random.uniform(-0.2, 0.2))
    return current_balance * rate

def save_to_file(data):
    """ Save the provided data to a CSV file """
    with open('retirement_savings.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Year", "Balance"])
        writer.writerows(data)

# Main program starts here
if __name__ == '__main__':
    print("Welcome to the Retirement Calculator!")
    
    try:
        age = int(input("Please enter your current age: "))
        retirement_age = int(input("Please enter your desired retirement age: "))
        savings = float(input("Please enter your current savings ($): "))
        annual_contribution = float(input("Enter your annual savings amount ($): "))
        rate_of_return = float(input("Enter your expected average rate of return (as a decimal, e.g. 0.05 for 5%): "))
        
        year_data = []

        for year in range(age, retirement_age):
            growth = calculate_annual_growth(savings, rate_of_return)
            savings += growth + annual_contribution
            print(f"Year {year + 1}: Projected balance: ${savings:.2f}")
            year_data.append((year+1, round(savings, 2)))
        
        withdrawal = savings * 0.04
        print(f"\nAt age {retirement_age}, your projected savings is: ${savings:.2f}")
        print(f"Recommended annual withdrawal (using 4% rule): ${withdrawal:.2f}")
        
        save_option = input("Would you like to save the results to a file? (yes/no): ").lower()
        if save_option == 'yes':
            save_to_file(year_data)
            print("Data has been saved to 'retirement_savings.csv'!")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

