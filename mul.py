def multiply(a, b):
    """
    Returns the product of two numbers.
    """
    return a * b

if __name__ == "__main__":
    num = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The product of {num} and {num2} is {multiply(num1, num2)}")