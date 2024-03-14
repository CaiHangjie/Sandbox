# Part 1: Writing "name.txt"
user_name = input("Enter name: ")
with open("name.txt", 'w') as name_file:
    name_file.write(user_name)

# Part 2:  read and print
with open("name.txt", 'r') as name_file:
    name = name_file.read()
    print(f"Your name is {name}")

# Part 3: add together
with open("numbers.txt", 'r') as number_file:
    number1 = int(number_file.readline().strip())
    number2 = int(number_file.readline().strip())
    result = number1 + number2
    print(f"The sum of the first two numbers is: {result}")

# Part 4: calculate the total
total = 0
with open("numbers.txt", 'r') as numbers_file:
    for line in numbers_file:
        total += int(line.strip())

print(f"The total of all numbers is: {total}")
