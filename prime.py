__author__ = '1d4n'


def is_prime(num):
    factors = 0
    tester = 2
    while tester ** 2 <= num:
        if num % tester == 0:
            factors += 1
        tester += 1
    return factors == 0  # return True only if the number has no factors.


# Checking if the code is running from the current file (and not being imported from another file):
if __name__ == '__main__':
    while True:
        number = input("Please insert a number to check if it's a prime number (enter -1 to close): \n")
        if not number.isdigit():
            break
        if is_prime(int(number)):
            print("The number", number, "is prime.\n")
        else:
            print("The number", number, "is not prime.\n")

