def fibonacci(n):
    if n <= 0:
        raise ValueError("Number of terms must be positive.")
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

terms = int(input("Enter the number of terms: "))
try:
    print("Fibonacci sequence:", fibonacci(terms))
except ValueError as error:
    print("Error:", error)
