# Kyrian
# 9-24-2025
# P2LAB2
# This program uses a dictionary to store vehicles and their MPG(Miles Per Gallon) values.
# It lets the user pick a vehicle, then calculates how many gallons of gas 
# are needed for a given number of miles.

# Create dictionary with vehicles and their mpg.
vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Store and print the keys
keys = vehicles.keys()
print(keys)

# Prompt user for vehicle
vehicle_choice = input("Enter a vehicle to see its mpg: ")

# Display mpg for chosen vehicle
mpg = vehicles[vehicle_choice]
print(f"\nThe {vehicle_choice} gets {mpg} mpg.")

# Prompt user for miles
miles = float(input(f"\nHow many miles will you drive the {vehicle_choice}? "))

# Calculate gallons needed
gallons_needed = miles / mpg

# Display result rounded to 2 decimals
print(f"\n{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle_choice} {miles:.1f} miles.")
