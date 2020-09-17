__author__ = '1d4n'


def fib_0(n):
    """This functions returns a list which contains the first n numbers in the fibonacci sequence, starting with 0.
    Args:
        n = an positive integer.
    """
    if n.isdigit():
        if int(n) < 1:
            return "Error: the number of numbers must be at least 1"
        elif int(n) == 1:
            fib_list = [0]
        else:
            fib_list = [0, 1]
        while len(fib_list) < int(n):
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list


def fib_1(n):
    """This functions returns a list which contains the first n numbers in the fibonacci sequence, starting with 1.
    Args:
        n = an positive integer.
    """
    if n.isdigit():
        if int(n) < 1:
            return "Error: the number of numbers must be at least 1"
        elif int(n) == 1:
            fib_list = [1]
        else:
            fib_list = [1, 1]
        while len(fib_list) < int(n):
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list


if __name__ == '__main__':  # Checking if the code is running from the current file (and not being imported as a module)

    while True:
        number = input("How many numbers of the fibonacci sequence to you want to see? (enter 0 to stop)\n")
        if number == '0':
            break
        if fib_0(number) or fib_1(number) is not None:
            print("starting with zero:", fib_0(number))
            print("starting with one:", fib_1(number), "\n")
        else:
            print("Error: You must enter a positive number!\n")
