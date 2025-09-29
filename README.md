# comp163-assignment-5
# Challenge 1: Collatz sequence - while loop for unknown iterations
print("=== Challenge 1: Collatz Conjecture ===")

current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", end=" ")

# Loop until the sequence reaches 1
while current_number != 1:
    print(current_number, end=" ")
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = current_number * 3 + 1
    step_count += 1

# Print the final 1
print(current_number)

print("Steps:",step_count,"\n")

# Challenge 2: Prime checker - for loop for known range
print("=== Challenge 2: Prime Number Checker ===")

n = int(input("Enter a number: "))

print(f"Testing divisors from 2 to {n-1}...")

is_prime = True  # assume prime until proven otherwise

for divisor in range(2, n):  # check all numbers from 2 to n-1
    if n % divisor == 0:
        print(f"{n} is not prime (divisible by {divisor})")
        is_prime = False
        break  # stop as soon as a divisor is found

if is_prime:
    print(f"{n} is prime!","\n")
