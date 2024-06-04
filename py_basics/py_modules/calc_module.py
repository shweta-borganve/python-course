# calc_module.py

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference when b is subtracted from a."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient when a is divided by b. Raises ZeroDivisionError if b is zero."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

if __name__ == "__main__":
    # Test the functions with some examples
    print("Testing the calculation functions:")
    print(f"add(1, 2) = {add(1, 2)}")
    print(f"subtract(5, 3) = {subtract(5, 3)}")
    print(f"multiply(4, 3) = {multiply(4, 3)}")
    try:
        print(f"divide(10, 2) = {divide(10, 2)}")
        print(f"divide(10, 0) = {divide(10, 0)}")
    except ZeroDivisionError as e:
        print(e)
