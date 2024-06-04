# calc_module.py

def add(a, b): #this defines that adding a,b calling def the function
    """Return the sum of a and b."""
    return a + b

def subtract(a, b): #this defines that substrcting b,a calling def the function
    """Return the difference when b is subtracted from a."""
    return a - b

def multiply(a, b): #this defines that multipliying a,b calling def the function
    """Return the product of a and b."""
    return a * b

def divide(a, b): #this defines that dividing a,b calling the function
    """Return the quotient when a is divided by b. Raises ZeroDivisionError if b is zero."""
    if b == 0: #if b=0 it gives the zero divisio error
        raise ZeroDivisionError("division by zero")
    return a / b

if __name__ == "__main__":
    # Test the functions with some examples
    print("Testing the calculation functions:")
    print(f"add(1, 2) = {add(1, 2)}")
    print(f"subtract(5, 3) = {subtract(5, 3)}")
    print(f"multiply(4, 3) = {multiply(4, 3)}")
    try: #we using the try: method because to aviod the zero division error
        print(f"divide(10, 2) = {divide(10, 2)}")
        print(f"divide(10, 0) = {divide(10, 0)}")
    except ZeroDivisionError as e: #and we use the xcept method also.
        print(e) 
