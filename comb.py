
def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)

def binom(n, k):
    if isinstance(n, int) and isinstance(k, int) and n >= k >= 0:
        return int(fact(n) / (fact(k) * fact(n-k)))
    return 0

def solutions(n,m):
	"""
	:param n: the number of elements
	:param m: a natural number
	return: the number of natural solutions for: x_1 + x_2 +... x_n = m
	"""
	a = n -1 + m
	return binom(a, m)

if __name__ == "__main__":

    x = y = 1
    while True:
        if x >= 1 and y >= 0:
            print("x_1 + x_2 + x_3 + ... x_n = m")
            x = int(input("How many elements? (n = ?) "))
            y = int(input("What is the value of m? "))
            print("The number of natural solutions for the equation is:", solutions(x, y))

            z = 0
            for i in range(y+1):
                z += solutions(x-1, i)
            print(" The number of natural solution for: x_1 + x_2 + x_3 + ... x_n-1 <= m is:", z)

            again = int(input("Again? (0 = No \ 1 Yes) "))
            if not again:
                break
