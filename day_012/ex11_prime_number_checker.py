def is_prime(num):
    """
    Check if a number is a prime number.

    :param num: The number to check for primality.
    :return: True if the number is prime, False otherwise.
    """
    if num == 2:
        return True
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(is_prime(73))
print(is_prime(75))
