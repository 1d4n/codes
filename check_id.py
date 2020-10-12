__author__ = '__1d4n__'


def check_digit(number):
    """Calculates the Check-Digit of the ID number
    :param number: An ID number without a Check-Digit
    :return: The Check-Digit
    """
    digits_sum = 0
    for i in range(len(number)):
        if not number[i].isdigit():
            return "please enter only numbers."
        p = int(int(number[i]) * (int(i) % 2 + 1))
        if p > 9:
            p -= 9
        digits_sum += p
    return 10 - digits_sum % 10 if digits_sum % 10 else digits_sum % 10


# One line:
def get_check_digit(num: str):
    digits_sum = sum([sum(map(int, str(int(num[i]) * (i % 2 + 1)))) for i in range(len(num))]) % 10
    return 10 - digits_sum if digits_sum % 10 else digits_sum


def is_valid_id(num) -> bool:
    # return sum([sum(map(int, str(int(num[i]) * (i % 2 + 1)))) for i in range(len(num))]) % 10 == 0 and len(num) == 9
    return sum([(int(d) * (i % 2 + 1) - 9) if (int(d) * (i % 2 + 1) > 9) else (int(d) * (i % 2 + 1)) for i, d in enumerate(f"{'0' * (9 - len(str(id_num)))}{id_num}")]) % 10 == 0


if __name__ == '__main__':
    while True:
        id_number = input("\nPlease enter an ID number without the last digit: (enter -1 to close)\n")
        if id_number == '-1':
            break
        result = str(check_digit(id_number))
        if result.isdigit():
            print("The check digit is:", result)
            print("Full ID:", ''.join((id_number, result)))
        else:
            print(result)
