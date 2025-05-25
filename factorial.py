def find_factorial(num):
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    return factorial

print("The factorial of 5 is", find_factorial(5))