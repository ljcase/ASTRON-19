x = [0.0,3.0,5.0,2.5,3.7]
print(x[2])

x.pop(2)
print(x)

x.remove(2.5)
print(x)

x.append(1.2)
print(x)

y = x.copy()
print(y)
y.append(2.0)
print(y)
print(x)

print(y.count(0.0))
y.append(3.7)
print(y)
print(y.count(3.7))
print(y.index(3.7))

y.sort()
print(y)

y.reverse()
print(y)

y.clear()
print(y)