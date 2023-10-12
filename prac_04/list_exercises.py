# task 1

numbers = []
for i in range(5):
    numbers.append(float(input("Number: ")))

print(f"The first number is {numbers[0]:,.0f}")
print(f"The last number is {numbers[-1]:,.0f}")
print(f"The smallest number is {min(numbers):,.0f}")
print(f"The largest number is {max(numbers):,.0f}")
print(f"The average of the numbers is {sum(numbers)/len(numbers)}")

# task 2

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'] 

username = str(input("What is your username? "))
if username in usernames:
    print("Access granted")
else:
    print("Access denied")