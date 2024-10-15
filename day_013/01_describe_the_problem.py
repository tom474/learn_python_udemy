# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")
#
#
# my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# The for loop iterates over a range of numbers from 1 to 19.

# 2. When is the function meant to print "You got it"?
# The function is meant to print "You got it" when the variable `i` equals 20.

# 3. What are your assumptions about the value of i?
# The assumption is that `i` will eventually reach 20, but with the current range, it will not.

# Fix the code:
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()
