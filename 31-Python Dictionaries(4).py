#################################  Removing Items  #################################  

# Remove Dictionary Items  !

# There are several methods to remove items from a dictionary   !

is_dict = {

    "Name" : 'Ali' ,

    "LastName" : 'Outis' ,

    "ID" : 'Connell_Outis' ,

    "Email" : 'Imali.askari@outlook.com' ,

    "Site" : 'WWW.Github.Com'
} 

print(is_dict)             # Before

is_dict.pop("ID") 

print(is_dict)             # After

print('---------------------------------------------------------------------')  

# The popitem() method removes the last inserted item ( in versions before 3.7, a random item is removed instead )    ! 

is_dict.popitem()     # Last Item 

print(is_dict)  

print('---------------------------------------------------------------------')

# The del keyword can also delete the dictionary completely    !   

# Error ////  There is NO Index here

# del is_dict 

# print(is_dict)   

# print('---------------------------------------------------------------------') 

# The del keyword removes the item with the specified key name    ! 

del is_dict['LastName'] 

print(is_dict)  

print('---------------------------------------------------------------------') 

# The clear() method empties the dictionary     ! 

is_dict.clear() 

print(is_dict) 

print('---------------------------------------------------------------------') 








