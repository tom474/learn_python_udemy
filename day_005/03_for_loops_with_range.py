print(range(1, 10))  # Doesn't do anything

for number in range(1, 10):  # Print 1 to 9
    print(number)

for number in range(1, 11):  # Print 1 to 10
    print(number)

# Gauss Challenge
total = 0
for number in range(1, 101):
    total += number
print(total)
