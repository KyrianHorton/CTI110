# Kyrian Horton
# 10/19/2025
# P3HW2 s gross pay, including overtime pay if applicable.
'''
Pseudocode:
1. Ask user for employee name
2. Ask for number of hours worked
3. Ask for pay rate
4. If hours worked > 40:
overtime_hours = hours_worked - 40
overtime_pay = overtime_hours * (pay_rate * 1.5)
regular_pay = 40 * pay_rate
Else:
overtime_hours = 0
overtime_pay = 0
regular_pay = hours_worked * pay_rate
5. gross_pay = regular_pay + overtime_pay
6. Display all information formatted in columns
'''
# Input
name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
# Process
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate
gross_pay = regular_pay + overtime_pay
# Output
print("----------------------------------------------")
print("Employee name: ", name)
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15} {'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("--------------------------------------------------------------------------------------------------------")
print(f"{hours_worked:<15.1f}{pay_rate:<15.1f}{overtime_hours:<15.1f}{overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<14.2f}")