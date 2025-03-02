def binary_r(number):
    if number // 2 == 1:
        return str(number // 2) + str(number % 2)
    else:
        return binary_r(number//2) + str(number % 2) 
    
def binary_i(number):
    answer = ""
    while number // 2 != 1:
        answer = str(number % 2) + answer
        number = number//2
    return str(number // 2) + str(number % 2) + answer

print(binary_r(12))
print(binary_i(12))
        
        