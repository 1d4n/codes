__author__ = '__1d4n__'


def is_prime(n):
    """ Checks if an integer is a prime number
    Args:
        n = an integer
    """
    factors = 0
    test = 2
    while test * test <= n:
        if n % test == 0:
            factors += 1
        test += 1
    return factors == 0  # return True only if the number has no factors.


if __name__ == "__main__":

    while True:
        number = input("Please enter a number to check if it's a prime number (enter -1 to stop): \n")
        if number.isdigit():
            if is_prime(int(number)):
                print("The number", number, "is prime.\n")
            else:
                print("The number", number, "is not prime.\n")
        else:
            if int(number) == -1:
                break
            print("Error: You can only enter a number!\n")
