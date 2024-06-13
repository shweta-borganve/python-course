def factorial(n):
    if n<0:
        return "Invalid input.please enter a non-negative integer."
    if n==0 or n==1:
        return 1
    else:
       return n*factorial(n-1)

print(factorial(5))