#################################  Python ---> Change List Items  ################################# 

# To change the value of a specific item, refer to the index number  ! 

my_list = ['ali', 'outis','connell', 'askari','CNO','aliAskari','ConnellOutis']   

my_list[2] = 'Github' 

print(my_list) 

print('--------------------------------------------------------------------------------------------')  

# To change the value of items within a specific range, define a list with the new values , 

# and refer to the range of index numbers where you want to insert the new values  !

my_list[1:4] = ['w3schools', 'faradars', 'youtube']  

print(my_list) 

print('--------------------------------------------------------------------------------------------') 

my_list[1:2]  =  ['Python', 'Function'] 

print(my_list) 

print('--------------------------------------------------------------------------------------------') 

# If you insert less items than you replace, 
# the new items will be inserted where you specified, and the remaining items will move accordingly   !

my_list[4:8] = ['Hello World'] 

print(my_list) 

print('--------------------------------------------------------------------------------------------')  

##############################################################################
#################################  Insert()  #################################
##############################################################################

# To insert a new list item, without replacing any of the existing values, we can use the insert() method  !

# The insert() method inserts an item at the specified index  ! 

my_list.insert(6, 'Def') 

print(my_list) 

print('--------------------------------------------------------------------------------------------') 

print(len(my_list))

print('--------------------------------------------------------------------------------------------')  


