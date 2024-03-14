"""
CP1404/CP5632 - Practical
Answer the following questions:

1. When will a ValueError occur?
# An error occurs when the user enters a value that cannot be converted to an integer.

2. When will a ZeroDivisionError occur?
# If the user enters the denominator 0, an error occurs because dividing by zero is undefined.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, can change the code to check if the denominator is 0 before you perform the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
