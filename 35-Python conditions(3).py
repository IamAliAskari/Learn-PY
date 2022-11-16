#################################  Python If ... Else  ################################# 

# Short Hand If 

# If you have only one statement to execute, you can put it on the same line as the if statement    ! 

i = 5 

j = 12 

if i < j : print ('Ok !  i  less than  j') 

print('---------------------------------------------------------------------') 

# Short Hand If ... Else 

# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line   ! 

x = 4 

y = 5 

print('x  less than  y') if  x < y else print('y  less than  x')  

print('---------------------------------------------------------------------') 

# AND 

# The and keyword is a logical operator, and is used to combine conditional statements   !

n = 2 

m = 3 

l = 5 

if n < m and m < l :

    print('Ok !  n  less than  m  and  m  less than  l')  

print('---------------------------------------------------------------------')

# OR 

# The or keyword is a logical operator, and is used to combine conditional statements    ! 

c = 4 

w = 8 

q = 10 

if c < q or w < q :

    print('The number  q  is the largest number') 

print('---------------------------------------------------------------------')

# Nested If 

# You can have if statements inside if statements, this is called nested if statements     ! 

f = 55 

if f < 60 :

    if f < 56 : 

        if f < 90 : 

            if f > 54 :

                print (' f == 55 ') 

print('---------------------------------------------------------------------') 