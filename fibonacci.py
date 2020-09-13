__author__ = '1d4n'


def fib_0(n):
    # This functions returns a list which contains the first n numbers in the fibonacci sequence, starting with 0.
    if n < 1:
        return "Error: the number of numbers must be at least 1"
    elif n == 1:
        fib_list = [0]
    else:
        fib_list = [0, 1]
    while len(fib_list) < n:  # Repeat this until the number of items in the list is less than the number of the input.
        while True:  # Adding the next number in the fibonacci sequence to the list and than go back to the first loop.
            fib_list.append(fib_list[-1] + fib_list[-2])
            break
    return fib_list


def fib_1(n):
    # This functions returns a list which contains the first n numbers in the fibonacci sequence, starting with 1.
    if n < 1:
        return "Error: the number of numbers must be at least 1"
    elif n == 1:
        fib_list = [0]
    else:
        fib_list = [1, 1]
    while len(fib_list) < n:  # Repeat this until the number of items in the list is less than the number of the input.
        while True:  # Adding the next number in the fibonacci sequence to the list and than go back to the first loop.
            fib_list.append(fib_list[-1] + fib_list[-2])
            break
    return fib_list


if __name__ == '__main__':  # Checking if the code is running from the current file (and not being imported as a module)
    number = int(input("How many numbers of the fibonacci sequence to you want to see? "))
    print("starting with zero:", fib_0(number))
    print("starting with one:", fib_1(number))
