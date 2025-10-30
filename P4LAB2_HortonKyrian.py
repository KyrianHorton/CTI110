# This program displays a multiplication table for a non-negative integer.
run_again = "yes"

while run_again.lower() == "yes":
    num = int(input("Enter an integer: "))

    if num < 0:
        print("\nThis program does not handle negative numbers.\n")
    else:
        print()
        for i in range(1, 13):
            print(f"{num} * {i} = {num * i}")
        print()

    run_again = input("Would you like to run the program again? ")
    print()

print("Exiting program...")
