def palindrome(string):
    if len(string) == 1:
        return string
    else:
        return palindrome(string[1:len(string)]) + string[0]
    
print(palindrome("ary"))