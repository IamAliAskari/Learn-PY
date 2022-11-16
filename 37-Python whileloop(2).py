#################################  Python While Loops  #################################

# The break Statement   ::::: 

# With the break statement we can stop the loop even if the while condition is true     ! 

a = 1 

while a < 8 :

    print(a) 

    if a == 5 :

        break

    a += 1

print('---------------------------------------------------------------------') 

# The continue Statement   ::::: 

# With the continue statement we can stop the current iteration, and continue with the next    ! 

b = 1 

while b < 10 :

    b += 1 

    if b == 6 :

        continue 

    print(b) 

print('---------------------------------------------------------------------')

# The else Statement    :::::

# With the else statement we can run a block of code once when the condition no longer is true     ! 

s = 1 

while s < 10 :

    print(s) 

    s += 1 

else :

    print('The commands were executed up to 9 and then the commands hit ,\n--False--  and the  --Else--  command was executed ! ') 

print('---------------------------------------------------------------------') 