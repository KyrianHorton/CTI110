# Kyrian Horton
# 10-5-2025
# P2HW2_HortonKurian
# This program asks the user to enter grades for six modules,
# stores them in a list, and then displays the lowest, highest,
# sum, and average of those grades formatted neatly.
# --------------------------------------------
# Pseudocode:
# 1. Ask user to enter six grades (Modules 1–6)
# 2. Store all six grades in a list called module_grades
# 3. Use built-in functions to calculate:
# - lowest grade using min()
# - highest grade using max()
# - sum of grades using sum()
# - average using sum() / len()
# 4. Display results formatted like the example:
# - Two decimals for average
# - One decimal for grades
# --------------------------------------------
# Input Section
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))
# Store grades in a list
module_grades = [grade1, grade2, grade3, grade4, grade5, grade6]
# Calculations
lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)
# Output Section
print("\n------------Results------------")
print(f"{'Lowest Grade:':20s}{lowest:.1f}")
print(f"{'Highest Grade:':20s}{highest:.1f}")
print(f"{'Sum of Grades:':20s}{total:.1f}")
print(f"{'Average:':20s}{average:.2f}")
print("-------------------------------")
