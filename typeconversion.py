#-------------------- TYPE CONVERSION-------------------
# convertion one datatype into another datatype is called type conversion
# types of type conversion\\
#  implicit type conversion\
#  explicit type coinversion


                              # implict type conversion :
# # in the implicit type conversion python automatically convert 
 # one data type into another data type 
a = 5                        #  its int type 
b = 2                       # its a int datatype
data = a/b
print(data)               # but the answer is in decimals means float data type 
# so here the converstion of integer data type into float data type 


# ----------------------------explicit type conversion------------------

#in the cast/ explicit type conversion ,programmer converts one data type into another 
# data type 
#int(n) 
# float(n) 
# complex(n)
# complex(x,y) where x is real part and y is imaginary part
# str(n) 
# list(n) 
# tuple(n) 
# bin(n)
#oct(n)
# hex(n)
#  examples
a = 5    # its a int  type
b = 2    
data = a/b    #but after division the answer will be in float datatype but
#we want the answer in int data type so the procedure is :
data = a/b
int_data = int(data)
print(int(data))
# so its convert the float type into int type 

# float to integer 
n = 10.36
convert = int(n)
print(convert)

#integer to float 
a = 10 
b = 20 
c = a + b 
cng = float(c)
# strinf to tuple 
a = " my name is umar "
conv = tuple(a)

# string to list 
a = "my name is umar "  
convert = list(a)
# integer to binary 
a = 20 
convert = bin(a)
