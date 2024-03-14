total = 0
item_num = int(input("Number of items: "))
for i in range(item_num):
    item_price = float(input("Price of item: "))
    while item_price < 0:
        print("Invalid items!")
        item_price = float(input("Price of item: "))
    total += item_price

if total > 100:
    total *= 0.9

print(f"Total price for {item_num} items is ${total:.2f}")
