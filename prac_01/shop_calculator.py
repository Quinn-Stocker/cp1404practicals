total_price = float(0)
valid_input = False
while valid_input == False:
    num_of_items = int(input("Number of Items: "))
    if num_of_items > 0:
        valid_input = True
    else:
        print("Invalid number of items!")

for i in range(0, num_of_items, 1):
    total_price = total_price + float(input(f"Price of Item #{i+1}: $"))
print()

if total_price > 100:
    final_price = total_price * 0.9
else:
    final_price = total_price

print(f"Total Price for {num_of_items} items is ${final_price:.2f}")