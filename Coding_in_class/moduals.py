import numpy as np
import matplotlib.pyplot as plt
import sys
import os

n=10
print(f"at first,n={n}")
print(sys.argv)
print(os.getcwd())
if (len(sys.argv)>1):
    n = int(sys.argv[1])
    print(f'now, n = {n}')
