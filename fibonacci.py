__author__ = '1d4n'


def fibonacci():
    a, b = 0, 1  # First 2 numbers in the fibonacci sequence
    while True:
        a, b = b, a + b
        yield a


if __name__ == '__main__':
    while True:
        num = input("\nHow many numbers of the fibonacci sequence do you want to see? (0 to stop)\n")
        if num == '0' or not num.isdigit():
            break
        fib_generator = fibonacci()
        for i in range(int(num)):
            print(next(fib_generator), end=" ")
