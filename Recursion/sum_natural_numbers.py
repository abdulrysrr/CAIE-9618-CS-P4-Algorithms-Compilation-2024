def sum_r(n):
    if n == 0:
        return n
    else:
        return n + sum_r(n-1)

def sum_i(n):
    sum = 0
    for x in range(n+1):
        sum += x
    return sum
    
print(sum_r(10))
print(sum_i(10))