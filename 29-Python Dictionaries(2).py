#################################  Dictionaties Itemes  ################################# 

my_dict = {

    "Name" : 'Ali' , 

    "Email" : 'Imali.askari@outlook.com' ,

    "Age" : 21 ,

    "LastName" : 'Outis'  ,

    "from" : 'Github'

}  

myname = my_dict["Name"]  

print(myname)   

print('---------------------------------------------------------------------')  

#######  Get()  #######  

# There is also a method called get() that will give you the same result   !

my_name = my_dict.get("from") 

print(my_name) 

print('---------------------------------------------------------------------') 

#######  keys()  ####### 

# The keys() method will return a list of all the keys in the dictionary    ! 

my_key = my_dict.keys() 

print(my_key)  

print('---------------------------------------------------------------------')  

#######  values()  ####### 

# The values() method will return a list of all the values in the dictionary    !

my_value = my_dict.values() 

print(my_value) 

print('---------------------------------------------------------------------')  

#######  items()  #######

#The items() method will return each item in a dictionary, as tuples in a list   ! 

my_iteme = my_dict.items() 

print(my_iteme)

print('---------------------------------------------------------------------')   

#######  if Key Exists  ####### 

# To determine if a specified key is present in a dictionary use the in keyword    !

if "Email" in my_dict :

    print("True") 

if "Ali" in my_dict :

    print('Ture') 

else :

    print('False')  

print('---------------------------------------------------------------------')   


 

