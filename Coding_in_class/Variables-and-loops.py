import numpy as np #we use numoy for klots of things

def main():
    i = 0           #integers can be declaerd with a number
    n = 10          #this is another integer
    x = 19.0        #floting point number because it has a number

    #we use numpy to declare arrays quickly

    y = np.zeros(n,dtype=float) #declares 10 0zeros as float using np

    #we can use fofr loop to iterate with a variable

    for i in range(n):       #i in tange [0,n-1]
        y[i] = 2.0 * float(i) + 1.      #set y = 2i+1 as floats

        #we can also simply iterate through a variable
    for y_element in y:
        print (y_element)

#exicute main element
if __name__== "__main__":
    main()
