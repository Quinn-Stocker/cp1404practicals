"""
1.  Write code that asks the user for their name,
    then opens a file called "name.txt" and writes that name to it. 
    Remember to close your file.
""" 

OUTPUT_FILE = "name.txt"

name = input("What is your name? ")

out_file = open(OUTPUT_FILE, 'w')

print(name, file = out_file)

out_file.close()

"""
2.  (In the same file, but as if it were a separate program)
    Write code that opens "name.txt" and reads the name (as above) then prints,
    "Your name is Bob" (or whatever the name is in the file).
"""

INPUT_FILE = "name.txt"

in_file = open(INPUT_FILE, 'r')

print("Your name is ", in_file.read())

in_file.close()

"""
3.  Create a text file called numbers.txt and save it in your prac directory. 
    Put the following three numbers on separate lines in the file and save it:
        17
        42
        400
    Write code that opens "numbers.txt", 
    reads only the first two numbers and adds them together then prints the result, which should be... 59
"""

INPUT_FILE = "numbers.txt"

in_file = open(INPUT_FILE, 'r')

number_1 = int(in_file.readline())
number_2 = int(in_file.readline())

print(number_1 + number_2)

in_file.close()

"""
4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers
"""

INPUT_FILE = "numbers.txt"

sum_of_numbers = 0

in_file = open(INPUT_FILE, 'r')

for line in in_file:
    sum_of_numbers += int(line.strip())

print(sum_of_numbers)

in_file.close()

