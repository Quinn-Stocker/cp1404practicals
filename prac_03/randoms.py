import random

print(random.randint(5, 20))  # line 1

# The Smallest number that could possibly be seen was 5, whilst the largest was 20

print(random.randrange(3, 10, 2))  # line 2

# The Smallest number that could possibly be seen was 3, whilst the largest was 9
# 4 would not have been possible due to the step being 2, meaning that all values would have to stay as the same parity, odd

print(random.uniform(2.5, 5.5))  # line 3

# The Smallest number that could possibly be seen was 2.5, whilst the largest was 5.5

print(random.randint(1, 100)) # written code