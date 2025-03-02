def Calculate(Number):
    Value = -10
    for count in range(1,Number+1):
        Value = Value * count
    return Value

print(Calculate(3))