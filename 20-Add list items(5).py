#################################  Python ---> Add List Items  ################################# 

##############################################################################
#################################  append()  #################################
############################################################################## 

# To add an item to the end of the list, use the append() method  ! 

mylist = ['Ali', 'Askari', 'Connell'] 

mylist.append('Outis') 

print(mylist)  

print('--------------------------------------------------------------------------------') 


##############################################################################
#################################  insert()  #################################
##############################################################################  

# To insert a list item at a specified index, use the insert() method  !

# The insert() method inserts an item at the specified index  !

mylist.insert(0, 'CNO') 

print(mylist) 

print('--------------------------------------------------------------------------------')  


##############################################################################
#################################  extend()  #################################
############################################################################## 

# To append elements from another list to the current list, use the extend() method  ! 

new_list = ['one', 'two', 'three']  

mylist.extend(new_list) 

print(mylist) 

print('--------------------------------------------------------------------------------')

# The extend() method does not have to append lists, you can add any iterable object { tuples, sets, dictionaries etc }  ! 


