def NumberPattern(Value1, Value2, EndValue):
    print(Value1)
    if Value1 <= EndValue:
        Temp = Value2
        Value2 = Value1
        Value1 = Value1 + Temp
        return NumberPattern(Value1, Value2, EndValue) + 1
    else:
        return 0

NumberPattern(1, 1, 10)
