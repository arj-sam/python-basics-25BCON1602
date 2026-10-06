def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter an integer: "))
print(f"{number} is a prime number." if is_prime(number)
      else f"{number} is not a prime number.")
