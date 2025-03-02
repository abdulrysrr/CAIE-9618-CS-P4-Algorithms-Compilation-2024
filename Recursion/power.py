def power_r(x, y):
    #we have to return x^y    
    if (y == 1):
        return x
    else:
        return x * power_r(x, y-1)
    
def power_i(x, y):
    answer = 1 
    for i in range(y):
        answer = answer * x
    return answer


print(power_r(8,3))
print(power_i(8,3))