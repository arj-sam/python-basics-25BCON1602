def calculate(a, b, operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    raise ValueError("Invalid operator.")

a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

try:
    print("Result:", calculate(a, b, operator))
except (ValueError, ZeroDivisionError) as error:
    print("Error:", error)
