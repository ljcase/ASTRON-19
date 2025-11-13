try:
    print(a)
except:
    print("a is defined")

try:
    print(a)
except NameError:
    print("Variable 'a' is not defined")
except:
    print("Something is wrong")


print(a)