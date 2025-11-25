# Kyrian
# 11/25/2025
# P5LAB 
# This program simulates a self-checkout machine that generates a random amount owed and calculates the correct change using dollars and coins.

import random

def disperse_change(change):
    """Takes a float amount of change and prints the number of each coin needed."""
    
   
    cents = int(round(change * 100))

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    print()
    print(f"{dollars} Dollars")
    print(f"{quarters} Quarters")
    print(f"{dimes} Dimes")
    print(f"{nickels} Nickels")
    print(f"{pennies} Pennies")


def main():
    # Generate random total owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe ${amount_owed}")

    # Get user payment
    cash = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change
    change = round(cash - amount_owed, 2)

    # Display change
    print(f"Change is: ${change}")

    # Call function to disperse coins
    disperse_change(change)


# Call main function
main()
