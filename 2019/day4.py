import json

# --- Day 4: Secure Container ---

# Six-digit number

# The value is within the range given in your puzzle input.

# Two adjacent digits are the same (like 22 in 122345).

# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).

# How many different passwords within the range given in your puzzle input meet these criteria?

with open("2019/day4.json") as file:
    puzzle_input = json.load(file)

low = puzzle_input["LOW"]
high = puzzle_input["HIGH"]

def validator(n):
    if low <= n <= high:
        print("Pass: Within range")
    else:
        print("Fail: Not within range")
        return None

    # Default values, will be checked later
    has_adjacent_digits = False
    digits_never_decrease = True

    last_digit = n % 10
    n //= 10  # Remove last digit from n

    while n > 0:
        digit = n % 10  # Get last digit of n
        if digit == last_digit:
            has_adjacent_digits = True
        elif digit > last_digit:
            digits_never_decrease = False

        last_digit = digit
        n //= 10  # Remove last digit from n

    if has_adjacent_digits:
        print("Pass: Has at least two identical adjacent digits")
    else:
        print("Fail: Does not have at least two identical adjacent digits")

    if digits_never_decrease:
        print("Pass: Digits never decrease from left to right")
    else:
        print("Fail: Digits decrease from left to right")

    if digits_never_decrease and has_adjacent_digits:
        return True

    else:
        return False

count = 0
for n in range(low, high + 1):
    if validator(n):
        count += 1

print(count)
print(f"Probability of guessing the code: 1/{count} = {1/count*100}%")