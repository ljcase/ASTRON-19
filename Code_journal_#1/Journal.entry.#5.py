#Write a Python program that writes out a 
# table of the function sin(x) vs. x, 
# where x is tabulated between 0 and 2pi with
# a thousand entries. Follow the basic Python 
# program structure, including a main program
# function.

import numpy as np
import sys
import math
import matplotlib.pyplot as plt

def main():
    x = np.linspace(start=0, stop=2*np.pi, num=1000)
    y = np.sin(x)

    print("  x          sin(x)  ")
    print("------------------------------")
    for i in range(len(x)):
        print(f"| {x[i]:.5f},       {y[i]:.5f} |")

    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.savefig("sinplot.png",bbox_inches="tight")
    #plt.savefig("sinplot.png")
if __name__ == "__main__":
    main()

        

