# calculate.py

import calc_module

def main():
    """Main function to demonstrate the usage of calc_module functions."""
    a = 10
    b = 5
    
    # Demonstrate addition
    result_add = calc_module.add(a, b)
    print(f"calc_module.add({a}, {b}) = {result_add}")  # Output: 15

    # Demonstrate subtraction
    result_subtract = calc_module.subtract(a, b)
    print(f"calc_module.subtract({a}, {b}) = {result_subtract}")  # Output: 5

    # Demonstrate multiplication
    result_multiply = calc_module.multiply(a, b)
    print(f"calc_module.multiply({a}, {b}) = {result_multiply}")  # Output: 50

    # Demonstrate division
    result_divide = calc_module.divide(a, b)
    print(f"calc_module.divide({a}, {b}) = {result_divide}")  # Output: 2.0

    # Demonstrate division by zero error handling
    try:
        calc_module.divide(a, 0)
    except ZeroDivisionError as e:
        print(f"Error: {e}")  # Output: division by zero

if __name__ == "__main__":
    main()
