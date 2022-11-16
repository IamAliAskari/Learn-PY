#################################  Change Dictionary Items  ################################# 

# Change Value

my_dict = {

    "Brand" : 'Winston' , 

    "Model" : 'Mix' , 

    "Nicotin" : 0.8
} 

print(my_dict) 

my_dict ["Nicotin"] = 0.9 

print(my_dict) 

print('---------------------------------------------------------------------')   

##########  Update Dictionary  ##########

# The update() method will update the dictionary with the items from the given argument   !

# The argument must be a dictionary, or an iterable object with key:value pairs   !

my_dict.update({"Model" : 'Oltra'}) 

print(my_dict) 

my_dict.update({"Friend" : 'Ashkan'}) 

print(my_dict) 

my_dict ["Best Friend"] = 'Dany'  

print(my_dict) 

print('---------------------------------------------------------------------') 

# my_dict ["model"] = 'Good'               ################## Change 
                                                #       ||       #
# my_dict.update({"model" : 'Good'})       ################## Change  


