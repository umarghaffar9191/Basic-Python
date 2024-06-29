#bismillah irrahman irraaheem
#    none type

# jab koi b object koi b value contain nhi krta ha tu usy none datatype kehty hein

#    NUMERIC DATA TYPE

# #following are the numeric datatype 
#   int
#   float
#    complex
 
 #--------------------------------Int---------------------------------------------
 # the int datatype represents an integer nummber . an integer number without any decimal point
 # or fraction part in python it is possible to store very integer number as there is no limit 
 # for the sixe of an int datatype
# foor example 
#   20 ,30,344,-4545,454,-6666542453454
#    UMAR15 = 134413434
#    student_age = 23

 
 #---------------------------------float---------------------------------------
 #the floatdata type represents floating pointsnumbers a floating points numbers is a number that contains a 
 # decimal point
 #example
#         35.5 ,42335.55 ,
#    value = 5.1e5             its mean 5.1 10 ki power 5

# for check the type of the float open the terminal and write 
#   for example 
#    price  = 45.5
#    type(price)    it will give you the type of the variable


#--------------complex----------------------
# a complex number is a number thsat written in the form of a a+bj or a+BJ
#  a = real part of the number 
#   b = imaginary part of the number
# j or J = square root value of -1
# a nd v may contain integer or float number
# example 5+7j , 5.5+5j

# ------------------------------bool datatype----------------
#  bool data type represents boolean value true or false . python internally represents true as 1 
# and fal;se as 0
#  for example 
#     true + true = 2
#      truse - false = 1

# -----------------------sequence type--------------------------------
# following are sequence types
# string 
# list 
# tuple
# range
# ---------------------string --------------
# string reprsents group of characters , strings are enclosed in double quotes or single quotesum
# foe example
#  str1 = "my name is umar "         double quotes
#  helo = 'how are you'                single quotes

#-----------------list-------------------------------
# a list represemts a group of elements . a list can store diferent types of elements
# which can e modified . lists are dynamic which means size is not fixed .\ list are represents using 
#square bracket  []


# for example = [10,20,-50,34.5,"my name is khan and im not terrorist"]


#asan alfaz mein upper di gai example mein 5 different type of elememnts hein 
# ye sare elements aik an aik indexx par pare hua hein like 10 ka index number ha 0 
# 20 ka ha 1 esi trhan last string datatype ka number ha 4 
# yahan samajne wali bat ye ha k ye 0 sayu start hoon gay 

# question ye ata ha k agar last day value ka index number rpata kran ho to tab kia kiya jaye 
# to us k liya hum last say start karein gay like or agar hum start say surrunkarein to 0 say
#Start karein gay or jab last say start karein gay to -1 say start karein gay 



# foe example 
data = [20 , 30, 46 ,67 ]
print(data)
data[1] 
# if we want to chamge the value of the index then we follow the follwing method
data[1] = 335
print(data[1])

#--------------------SEQUENCE TYPE ( TUPLE )----------------------
#    tuple contain a group of elements which can be different types it is similar to
# list but typles are read only which means we can not modify its element tuples are
# represented using parentheses()
#EXAMPLE
#   DATA = (10 ,20 ,30,40 ,50 ,234 ,"MY NAME IS UMAR ")

data1 = (230, 330, 34.4, "hello")
print(data1)

# note : but here in tuple we can not change the value but in opposite in list we can change the value 

# if we want to know about the type of variable we know thatwe use use the following ,ethod 
type(data1)

#----------------------------RANGE------------------------------
# range represents the sequences of numbers in the range are not modified
# example 
#   rg =  range(5)

# ------------------set--------------
# SET IS   unordered forn or es mein mein same value dubara use nhi k sakte or ismein index 
# b nhi le sakate kyun ye order mein nhi hota 
 # ex 
data1 = {10, 20 , 30 , "umar "}

# -------------------MAPING\ DICT\ DICTIONATRY----------
# mapi represents a group of elements in the form of key value pairs
# EXAMPLE
data = {101: 'umar',102: 'eman'}
data2 = {'umar': 2000, 'eman':4000}



#     note : we use 
# square bracket[ ] for list      #( is mein index ki values chamge kr sakte hein)
# parentheses'/simple ( ) bracket for tuple     ( es mein nhi change kr sakhte)
# carlie bracket { }for set                   ( ye unirdered hota ha es mein index liya he nhi ja sakta )
#{ }for maping    ( a map represents a group of elements in the form of key values)

