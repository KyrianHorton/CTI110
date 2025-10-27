# Kyrian Horton
# 9-24-2025
# P2LAB1 Instructions
# This program takes the radius of a circle from the user and calculates
# the diameter, circumference, and area using circle formulas.

import math

# Get radius from user
radius = float(input("Enter the radius of the circle: "))

# Perform calculations
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Display results with required formatting
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")
