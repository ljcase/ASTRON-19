import numpy as np 

i = 10 #integer
print(type(i))   #print out the dtata type of i
 
a_i = np.zeros(i,dtype=int) #declar an array of ints
print(type(a_i))            #will return ndarray
print(type(a_i[0]))         #will return int64

x = 19.0                #flotig point number
print(type(x))          #print oout the dat ttype of x

y = 19e2                  #float 190 in scientific notation
print(type(y))           #print out the data type of x


z = np.zeros(i,dtype=float)    #declare array of float 
print(type(z))                 #will return nd array
print(type(z[0]))
                #will return float64