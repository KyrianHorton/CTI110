# Kyrian Horton
# 9-20-2025
# P1HW1_HortonKyrian
# This program calculates exponents and performs addition/subtraction using user input.

print("-----Calculating Exponenets----")

# Exponent section
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result = base ** exponent
print(f"\n{base} raised to the power of {exponent} is {result} !!\n")

print("-----Addition and Subtraction----")

# Addition and subtraction section
start = int(input("Enter a starting integer: "))
add_val = int(input("Enter an integer to add: "))
sub_val = int(input("Enter an integer to subtract: "))

final_result = start + add_val - sub_val
print(f"\n{start} + {add_val} - {sub_val} is equal to {final_result}")
