__author__ = '1d4n'


def check_digit(number):
        """Calculates the Check-Digit of the ID number
        Args:
        number (string)
        """
	digits_sum = 0
	for i, digit in enumerate(number, 0):
		if not digit.isdigit():
			return "Error: please enter only numbers."
		p = int(int(digit) * (int(i) % 2 + 1))
		if p > 9:
			p -= 9
		digits_sum += p
	if digits_sum % 10 == 0:
		return str(0)
	else:
		return str(10 - digits_sum % 10)


if __name__ == '__main__':
	id_number = ''
	while id_number != '0':
		id_number = input("Please enter an ID number without the last digit: (enter 0 to close)\n")
		while id_number != '0':
			result = check_digit(id_number)
			if result.isdigit():
				print("The check digit is:", result)
				print("Full ID:", ''.join((id_number, result)))
			else:
				print(result)
			print("")
			break
