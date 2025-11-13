s = "I am a string"
print(type(s))

yes = True
print(type(yes))

alpha__list = ["a","b","c"]
print(alpha__list)
print(type(alpha__list))
print(alpha__list[0])
print(type(alpha__list[0]))

alpha__list = [1.4,3.5,4.2]
print(alpha__list)
print(type(alpha__list))
print(alpha__list[0])
print(type(alpha__list[0]))

alpha__tuple = ("a","b","c")
print(type(alpha__tuple))

alpha__list[0] = "updated"
print(alpha__list)

alpha__list[0] = "updated"
print(alpha__tuple)

try:
    alpha__tuple[0] = "updated"
except TypeError:
    print("you cannot add elements to tuples")
print(alpha__tuple)
