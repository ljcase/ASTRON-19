import numpy as np


def main():

    x = np.linspace(0, 2* np.pi, 10)

    y_sin = np.sin(x)
    y_cos = np.cos(x)
    
    print("        sin(x)     cos(x)")
    print("-------------------------------------")
        
    for i in range(10): 
        print(f"{y_sin[i]:.5f}\t {y_cos[i]:.5f}")

if __name__ == "__main__":
    main()