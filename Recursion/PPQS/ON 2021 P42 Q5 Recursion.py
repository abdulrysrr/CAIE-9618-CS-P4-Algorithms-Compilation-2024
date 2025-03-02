def NonRecursive(Num1, Num2):
    Value = 0
    while Num1 < Num2:
        Value = Value + Num1
        Num1 = Num1 * 2
    if Num1 > Num2:
        Value = Value + 10
    else:
        Value = Value + Num1
    return Value
