# ==============================
# COMP 163: Assignment 5 - Loop Mastery
# Student: William Webster
# File: [WillWebster]_assignment_5.py
# ==============================
# Challenge 1 uses a while loop
# Challenge 2 uses a for loop
# Challenge 3 uses nested loops
# ==============================
# AI Assistance
# I used AI/Google Gemini to **clarify loop concepts** (why to use `while`, `for`, and nested loops).  
# I received suggestions on **code formatting and README structure**.  
# I wrote, tested, and understood all algorithms myself.  
# AI was used only in a **limited support role** as allowed by the assignment policy. 
# --------------------------------
# Challenge 1: Collatz Conjecture
# --------------------------------
print("=== Challenge 1: Collatz Conjecture ===")

# Required variables
current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", end=" ")

# While loop is used because we do not know how many steps until n reaches 1
while current_number != 1:
    print(current_number, end=" ")

    # If current_number is even, divide by 2
    if current_number % 2 == 0:
        current_number //= 2
    # If odd, multiply by 3 and add 1
    else:
        current_number = current_number * 3 + 1

    # Count steps
    step_count += 1

# Print final 1 at the end
print(1)
print(f"Steps: {step_count}")

# Git commit: "Challenge 1: Collatz sequence - while loop for unknown iterations"


# --------------------------------
# Challenge 2: Prime Number Checker
# --------------------------------
print("\n=== Challenge 2: Prime Number Checker ===")

num = int(input("Enter a number: "))

# Check for valid input
if num <= 1:
    print(f"{num} is not prime (must be greater than 1).")
else:
    print(f"Testing divisors from 2 to {num - 1}...")

    is_prime = True  # Assume prime until proven otherwise

    # For loop is used because we know the exact range of divisors to test
    for divisor in range(2, num):
        if num % divisor == 0:
            print(f"{num} is not prime (divisible by {divisor})")
            is_prime = False
            break  # No need to keep testing
    if is_prime:
        print(f"{num} is prime!")

# Git commit: "Challenge 2: Prime checker - for loop for known range"


# --------------------------------
# Challenge 3: Multiplication Table
# --------------------------------
print("\n=== Challenge 3: Multiplication Table ===")

# Print header row
print("    ", end="")
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

# Outer loop for rows (1–10)
for row in range(1, 11):
    # Print row number at start of line
    print(f"{row:2} ", end="")

    # Inner loop for columns (1–10)
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")

    print()  # New line after each row

# Git commit: "Challenge 3: Multiplication grid - nested loops for 2D data"
