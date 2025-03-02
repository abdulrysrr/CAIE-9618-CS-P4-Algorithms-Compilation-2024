def sum_r(num):
    if len(str(num)) == 1:
        return num
    else:
        return int(str(num)[0]) + sum_r(int(str(num)[1:len(str(num))]))

    
def sum_i(num):
    sum = 0
    for digit in str(num):
        sum = sum + int(digit)
    return sum
    
    
print(sum_r(123))
print(sum_i(123))