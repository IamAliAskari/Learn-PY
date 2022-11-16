###############################################################################################################
###############################################################################################################
###############################################################################################################
#############################################    String Method's   ############################################
###############################################################################################################
###############################################################################################################
############################################################################################################### 


# Converts the first character to upper case


Outis = "ali is Connell "  

print(Outis.capitalize()) 

print('----------------------------------------------------------------')


# Converts string into lower case 


Connell = "ConNELl IS Cno" 

print(Connell.casefold()) 

print('----------------------------------------------------------------')


# Returns the number of times a specified value occurs in a string 


CNO = ' Im Ali Askari , Im Connell Outis , Im CNO' 

print(CNO.count('i')) 

print('----------------------------------------------------------------')


# Searches the string for a specified value and returns the position of where it was found 


Ali = 'Hello how are you to day ?' 

print(Ali.find('t'))   # Space in Index = True 

print('----------------------------------------------------------------') 


# Formats specified values in a string 

Askari = '{} is best friend {} and  is best friend {}' 

print(Askari.format('Mahan', 'Ali', 'Mahan')) 

print('----------------------------------------------------------------')


# Returns a trimmed version of the string 

ali = '           Ali Askari is Connell Outis              '

print(ali.strip(' '))

print('----------------------------------------------------------------') 


# Converts the first character of each word to upper case 

askari = 'im ali askari , ali askari is connell outis' 

print(askari.title())  

print('----------------------------------------------------------------')


# Converts a string into upper case 

outis = 'im connell , connell outis is ali askari' 

print(outis.upper()) 

print('----------------------------------------------------------------')  


