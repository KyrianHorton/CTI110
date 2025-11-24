# Program: Test Score Average Calculator
# This program asks for a user's name and three test scores,
# then calculates the average and displays whether the user passed or failed.

# Ask for user's name
name = input("Enter your name: ")

# Ask for three test scores
score1 = float(input("Enter your first test score: "))
score2 = float(input("Enter your second test score: "))
score3 = float(input("Enter your third test score: "))

# Calculate average
average = (score1 + score2 + score3) / 3

# Display average
print(f"\n{name}, your average score is {average:.2f}")

# Determine pass or fail
if average >= 60:
    print("Congratulations! You are passing.")
else:
    print("Sorry, you are failing.")
