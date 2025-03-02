def fibonacci_r(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci_r(n - 1) + fibonacci_r(n - 2)

def fibonacci_i(n):
    if n == 0 or n == 1:
        return n
    else:
        n1 = 0
        n2 = 1
        for i in range(n):
            temp = n1
            n1 = n2
            n2 = temp + n2
        return n1


for x in range(8):
    print(fibonacci_i(x), end=" ")
print("\n")

for x in range(8):
    print(fibonacci_r(x), end=" ")
