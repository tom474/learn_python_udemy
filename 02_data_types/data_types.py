# String
print("Hello")
print("Hello"[0])
print("Hello"[4])
print("123" + "456")

# Integer
print(123 + 456)
print(123_456_789)

# Float
print(3.14159)

# Boolean
print(True)
print(False)

# Type checking
num_char = len(input("What is your name?: "))
print(type(num_char))

# Type conversion
new_num_char = str(num_char)
print("Your name have " + new_num_char + " characters")

a = str(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))

two_digit_number = input("Enter a 2-digit number: ")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
two_digit_number = first_digit + second_digit
print(two_digit_number)
