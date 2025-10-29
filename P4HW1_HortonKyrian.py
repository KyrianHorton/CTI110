# Kyrian Horton
# 10-29-2025
# P4HW1_HortonKyrian
# This program asks the user how many scores they want to enter.
# It uses loops to collect and validate the scores (0–100).
# After collecting all scores, it drops the lowest score,
# calculates the average of the remaining ones, and determines
# the letter grade for that average.

# --------------------------------------------
# Pseudocode:
# 1. Ask user how many scores they want to enter.
# 2. Create an empty list to store valid scores.
# 3. Use a loop to:
#    - Prompt user for each score.
#    - Validate that it’s between 0 and 100.
#    - If invalid, show an error and ask again.
# 4. Once all valid scores are collected:
#    - Find the lowest score (min)
#    - Remove the lowest from the list
#    - Calculate the average of the modified list
# 5. Determine letter grade based on average:
#    - 90–100: A
#    - 80–89:  B
#    - 70–79:  C
#    - 60–69:  D
#    - below 60: F
# 6. Display:
#    - Lowest score
#    - Modified score list
#    - Average
#    - Letter grade
# --------------------------------------------

# Ask user for number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Create list to store scores
scores = []

# Loop to collect valid scores
for i in range(1, num_scores + 1):
    while True:
        score = float(input(f"Enter score #{i}: "))
        if score < 0 or score > 100:
            print("\nINVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            # ask again for same score number
        else:
            scores.append(score)
            break

# Process scores
lowest_score = min(scores)
scores.remove(lowest_score)
average_score = sum(scores) / len(scores)

# Determine letter grade
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

# Display results
print("\n------------Results------------")
print(f"Lowest Score  : {lowest_score:.1f}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {grade}")
print("-------------------------------")
