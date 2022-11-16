# String's (str) in Python :

# Strings :

# Strings in python are surrounded by either single quotation marks, or double quotation marks !

# You can display a string literal with the print() function :

print("Connell")

# 'Connell' is the same as "Connell"

print('Connell')

print('***********************************************************')

#################################  Strings are Arrays  #################################


# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters !

# However, Python does not have a character data type, a single character is simply a string with a length of 1  !

# Square brackets can be used to access elements of the string  !



#################################  Example  #################################


# Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, Ali"

print(a[1])

print('***********************************************************')


#################################  Looping Through a String  #################################


# Since strings are arrays, we can loop through the characters in a string, with a for loop  !

for x in "Askari":
  print(x)


print('***********************************************************')


#################################  String Length  #################################


# To get the length of a string, use the len() function  !

a = "Ali, Outis"

print(len(a))

print('***********************************************************')


#################################  Check String  #################################


# To check if a certain phrase or character is present in a string, we can use the keyword in  !

G = "Connell Outis is Ali Askari"

print("Ali" in G)

print('***********************************************************')


#################################  Check if NOT  #################################


# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in  !

H = "Connell Outis is Ali Askari"

print("Outis" not in H)

print('***********************************************************')



