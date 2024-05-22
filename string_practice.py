#   string exercises 
# 1- string length
# Write a Python program to calculate the length of a string

i = "my name is muhammad umar "
length_of_string = len(i)
print(length_of_string)
#another approch
print(f"the length of the string is :{length_of_string}")

# ---------------------------------------------------------

# 2- String Concatenation
# Write a Python program to concatenate two strings.
string1 = 'my name is'
string2 = 'Muhammad Umar'
concatenate_string = string1 +' '+ string2
# the string with space which is used between string1 and string 2 
#is for given  space between strings  
print(concatenate_string)

# --------------------------slicing-------------------------------------

#3-String Indexing/slicing of string
# Write a Python program to get a character from a string using indexing
i = "my name is Muhammad umar"
print(i[0]) # for getting the first character of string 
print(i[-1]) # for getting last charachter of the string
print(i[:7]) # for getting start to specific index xharaacter
print(i[::-1])# for reverse the whole string

# -----------------------------------------------------------------------------

# 4- String Case Conversion
# Write a Python program to convert a string to uppercase and lowercase
# upper case
i = "my name is Muhammad umar"
result = i.upper() # upper functionn will convert the whole string into upper case
print(result)
# lower case
result2 = i.lower()
print(result2)

# ---------------------------------------------------------------------------

# 5-String Replacement
# Write a Python program to replace a word in a string with another word

i = "my name is Muhammad umar"
replacing = i.replace('umar','usman')
# It will replace with string with the second given string
print(replacing)

# -----------------------------------------------------------------------------