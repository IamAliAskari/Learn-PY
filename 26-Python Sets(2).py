##################################################    Access Set Items   ###############################################  

# You cannot access items in a set by referring to an index or a key    !  

from tkinter import Y


The_set = {'Ali', 'Connell', 'Outis', 'Askari'}  

print('Connell' in The_set)  

print('CNO' in The_set) 

print('---------------------------------------------------------------------')   


##################################################    Add Set Items   ############################################### 

# Once a set is created, you cannot change its items, but you can add new items   !

# To add one item to a set use the """"""add()"""""" method    ! 

my_set = {'def', 'function', 'value', 'operator'}  

my_set.add('Object Orientrd') 

print(my_set)  

print('---------------------------------------------------------------------')  


##################################################    Update Set Items   ###############################################  

# To add items from another set into the current set, use the update() method    ! 

new_set = {'time', 'items', 'Logo', 'internet', 'Enter', 'Dictionery'}  

in_set = {'Ali', 'Hossein', 'Reza', 'Yegane', 'Athena', 'SONIYA', 'Ariya'}  

new_set.update(in_set)  

print(new_set)  

print('---------------------------------------------------------------------')  


# The object in the update() method does not have to be a set, it can be any iterable object ( tuples, lists, dictionaries etc  )    !

#   [  ]            &             (  )              &                 {  }    


##################################################    Remove Set Items   ###############################################  

# To remove an item in a set, use the remove(), or the discard() method     ! 

is_set = {'Bahram', 'Amir', 'Akbar', 'Ramtin' }   

is_set.remove('Akbar')  

print(is_set)  

print('---------------------------------------------------------------------')  

#  #  #  #  If the item to remove does not exist, discard() will  """NOT"""  raise an  ""Error"""    !  #  #  #  #  

This_set = {'Bahram', 'Amir', 'Akbar', 'Ramtin' }  

This_set.discard('mmad')  

print(This_set)  

print('---------------------------------------------------------------------')   

# You can also use the pop() method to remove an item, but this method will remove the last item   ! 

# Remember that sets are unordered, so you will not know what item that gets removed   ! 

# The return value of the pop() method is the removed item   ! 

its_set = {'time', 'items', 'Logo', 'internet', 'Enter', 'Dictionery'}  

its_set.pop() 

print(its_set)  

print('---------------------------------------------------------------------')   

###################################################################################################################

x =  {'time', 'items', 'Logo', 'internet', 'Enter', 'Dictionery'}  

x.clear() 

print(x) 

print('---------------------------------------------------------------------')  

###################################################################################################################

##################################################    Join Set Items   ############################################

i = {'a', 'b', 'c'}

j = {1, 2, 3, 4} 

y = i.union(j)  

print(y)  

print('---------------------------------------------------------------------')  

# You can use the union() method that returns a new set containing all items from both sets, 

# or the update() method that inserts all the items from one set into another    !

# Both union() and update() will exclude any duplicate items   ! 


