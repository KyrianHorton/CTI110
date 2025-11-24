# Kyrian Horton
 # 10-5-2025
 # P2HW1_HortonKyrian
 # This program calculates and displays travel expenses, formatted neatly in aligned columns.
 # Input Section
 
print("This program calculates and displays travel expenses")
budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))
 # Calculations
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses
 # Output Section
print("\n------------Travel Expenses------------")
print(f"{'Location:':20s}{destination}")
print(f"{'Initial Budget:':20s}${budget:,.2f}")
print(f"{'Fuel:':20s}${gas:,.2f}")
print(f"{'Accommodation:':20s}${accommodation:,.2f}")
print(f"{'Food:':20s}${food:,.2f}")
print("---------------------------------------")
print(f"\nRemaining Balance: ${remaining_balance:,.2f}")