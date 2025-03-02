def factorial_r(number):
    if number == 1 or number == 0:
        return number
    else:
        return number * factorial_r(number - 1)
    
def factorial_i(number):
    if number == 1:
        factorial = number
    else:
        factorial = 1
        for x in range(number, 0, -1):
            factorial = factorial * x
    return factorial
        
    
print(factorial_r(5))
print(factorial_i(5))