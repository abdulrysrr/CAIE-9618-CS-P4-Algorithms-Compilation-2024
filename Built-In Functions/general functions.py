# 1. print()
print("Hello, world!")

# 2. input()
name = input("Enter your name: ")
print("Hello,", name)

# 3. len()
my_list = [1, 2, 3, 4, 5]
print("Length of list:", len(my_list))

# 4. str()
num = 10
str_num = str(num)
print("String representation of num:", str_num)

# 5. int()
str_num = "10"
num = int(str_num)
print("Integer representation of str_num:", num)

# 6. float()
num = float(str_num)
print("Float representation of str_num:", num)

# 7. type()
print("Type of num:", type(num))

# 8. range()
my_range = range(5)
print("Range:", list(my_range))

# 9. list()
my_list = list(range(5))
print("List:", my_list)

# 10. tuple()
my_tuple = tuple(my_list)
print("Tuple:", my_tuple)

# 11. dict()
my_dict = dict(one=1, two=2, three=3)
print("Dictionary:", my_dict)

# 12. set()
my_set = set(my_list)
print("Set:", my_set)

# 13. abs()
num = -10
print("Absolute value of num:", abs(num))

# 14. round()
num = 3.14159
print("Rounded value of num:", round(num, 2))


# 15. enumerate()
for index, value in enumerate(my_list):
    print("Index:", index, "Value:", value)

# 16. chr()
print("Character representation of 65:", chr(65))

# 17. ord()
print("Unicode code point of 'A':", ord('A'))

# 18. format()
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

# 19. eval()
x = 5
print("Result of eval('x + 1'):", eval('x + 1'))
