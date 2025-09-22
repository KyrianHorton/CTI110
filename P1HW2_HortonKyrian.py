# Kyrian
# 9-20-2025
# P1HW2_HortonKyrian
# This program calculates travel expenses by asking the user for budget,
# destination, and expected costs (gas, accommodation, food). It then 
# displays expenses and the remaining balance.

"""
Pseudocode:
1. Display program purpose (calculate travel expenses)
2. Ask user to enter budget → store as integer
3. Ask user to enter travel destination → store as string
4. Ask user to enter amount for gas → store as integer
5. Ask user to enter amount for accommodation → store as integer
6. Ask user to enter amount for food → store as integer
7. Calculate total expenses = gas + accommodation + food
8. Calculate remaining balance = budget - total expenses
9. Display travel summary:
    - Destination
    - Initial budget
    - Expenses (fuel, accommodation, food)
    - Remaining balance
"""

print("This program calculates and displays travel expenses\n")

# Collect user inputs
budget = int(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = int(input("\nHow much do you think you will spend on gas? "))
accommodation = int(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = int(input("\nLast, how much do you need for food? "))

# Math calculations
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Output results
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}\n")
print(f"Fuel: {gas}")
print(f"Accommodation: {accommodation}")
print(f"Food: {food}\n")
print(f"Remaining Balance: {remaining_balance}")
