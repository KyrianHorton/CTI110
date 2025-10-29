# Kyrian Horton
# 10/29/2025
# P4HW2 - Pay Program
# This program calculates each employee's gross pay, including overtime,
# and keeps track of total regular pay, total overtime pay, and total gross pay
# for all employees entered.

# Pseudocode:
# 1. Initialize total overtime pay, total regular pay, total gross pay, and employee count to 0.
# 2. Ask the user for the employee's name.
# 3. While the name is not "Done":
#     a. Ask for hours worked and pay rate.
#     b. If hours > 40, calculate overtime hours and overtime pay.
#     c. Calculate regular pay and gross pay.
#     d. Display individual results for the employee.
#     e. Add overtime pay, regular pay, and gross pay to running totals.
#     f. Ask for the next employee's name.
# 4. When "Done" is entered, display totals and number of employees processed.

# ---- Program Start ----

# Initialize totals
total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

# Ask for first employee
employee_name = input('Enter employee\'s name or "Done" to terminate: ')

while employee_name != "Done":
    hours_worked = float(input(f'How many hours did {employee_name} work? '))
    pay_rate = float(input(f'What is {employee_name}\'s pay rate? '))

    # Calculate overtime
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay

    # Display employee results
    print("\nEmployee name:\t", employee_name)
    print()
    print("Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay")
    print("----------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}"
          f"{overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<.2f}")
    print()

    # Update totals
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # Ask for next employee
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Display summary
print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
