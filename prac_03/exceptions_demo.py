"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# 1. This will occur when either the Numerator or Denominator inputs are not valid numbers.

# 2. This will occur when the input for the Denominator is 0, therefore causing the code to try to divide by zero.

# 3. This possibility could be avoided by first using a conditional statement to check for a denominator of zero before performing the operation.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")