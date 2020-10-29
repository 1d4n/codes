def boom(divisor):
  n = 0
  while True:
    n += 1
    yield "BOOM!" if not n % divisor else n


if __name__ == "__main__":
  boom_generator = boom(7)
  for i in range(100):
    print(next(boom_generator))
