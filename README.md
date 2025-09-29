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

print("Steps:", step_count)
