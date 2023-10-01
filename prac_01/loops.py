# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()

# for i in range(0, 101, 10):
#     print(i, end=' ')
# print()

# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()

# num = int(input("Number of Stars: "))
# for i in range(0, num, 1):
#     print("*", end=' ')
# print()

num = int(input("Number of Stars: "))
for i in range(0, num, 1):
    for j in range(0, i + 1, 1):
        print("*", end=' ')
    print()
print()