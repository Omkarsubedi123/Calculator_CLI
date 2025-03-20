# division.py
def add(a, b):
    return a+b
def divide(a, b):
    """Returns the result of division, handling division by zero."""
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the dividend: "))
        num2 = float(input("Enter the divisor: "))
        
        result = divide(num1, num2)
        print(f"The result of {num1} ÷ {num2} is {result}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

