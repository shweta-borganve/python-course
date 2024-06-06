#from calc_module import process_numbers, average, difference
#import calc_module
from calc_module import add, subtract, multiply

def main():
    result = add(2,3)
    print(result)

    result = subtract(5, 7)
    print(result)

    result = multiply(5, 6)
    print(result)

if __name__ == "__main__":
    main()