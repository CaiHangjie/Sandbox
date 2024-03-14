
numbers = [3, 1, 4, 1, 5, 9, 2]

# What values do the following expressions have?
print(numbers[0])        # Answer: 3
print(numbers[-1])       # Answer:2
print(numbers[3])        # Answer: 1
print(numbers[:-1])      # Answer: [3, 1, 4, 1, 5, 9]
print(numbers[3:4])      # Answer: [1]
print(5 in numbers)      # True
print(7 in numbers)      # False
print("3" in numbers)    # False
print(numbers + [6, 5, 3])  # Answer:[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# In the same Python file, write statements to achieve the following:
numbers = ["ten", 1, 4, 1, 5, 9, 1]

print(numbers[2:])
print(9 in numbers)
