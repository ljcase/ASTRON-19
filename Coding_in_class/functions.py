import numpy as np
import sys

x=1
print(np.exp(x))



def expo(x):
    return np.exp(x)

print(expo(x))

def add_two(x):
    y = x+2
    return y

input = 3
print(add_two(input))

output = add_two(input)
print(output)


def show_expo(n):
    for i in range(n):
        print(expo(float(i)))

show_expo(8)

print("\n\n\n\n\n\n\n")

def main():
    n = 10

    if (len(sys.argv) > 1):
        n = int(sys.argv[1])



    show_expo(n)


if __name__ == "__main__":
    main()