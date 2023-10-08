numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0]

# Output = 3

numbers[-1]

# Output = 2

numbers[3]

# Output = 1 (2nd 1)

numbers[:-1]

# Output = [3, 1, 4, 1, 5, 9]

numbers[3:4]

# Output = [1]

5 in numbers

# Output = True

7 in numbers

# Output = False

"3" in numbers

# Output = False

numbers + [6, 5, 3]

# Output = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# In the same Python file, write statements to achieve the following:

# 1. Change the first element of numbers to "ten" (the string, not the number 10)

numbers = ["ten"] + numbers[1:]

# 2. Change the last element of numbers to 1

numbers = numbers[:-1] + [1]

# 3. Print all the elements from numbers except the first two (slice)

print(numbers[2:])

# 4. Print whether 9 is an element of numbers

print(f"it would be {9 in numbers} to say that 9 is an element of numbers")