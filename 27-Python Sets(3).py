##################################################    intersection_update()   ############################################ 

# The intersection_update() method will keep only the items that are present in both sets    ! 

in_set = {'ali', 'CNO', 'Outis'}  

is_set = {'ASK', 'Outis', 'Connell'}  

in_set.intersection_update(is_set)  

print(in_set)  

print('---------------------------------------------------------------------')  

# The intersection() method will return a new set, that only contains the items that are present in both sets    !

myset = {'Ali', 'Askari', 'Reza'}  

my_set = {'Sina', 'Askari', 'Reza'}  

z = myset.intersection_update(my_set)  

print(z)  

print('---------------------------------------------------------------------')   


# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets   !

you_set = {'Ali', 'Askari', 'Reza'}  

your_set = {'ASK', 'Outis', 'Connell'} 

you_set.symmetric_difference_update(your_set)  

print(you_set)  

print('---------------------------------------------------------------------')   


































