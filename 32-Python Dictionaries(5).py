#################################  Copy Dictionaries  ################################# 

# You cannot copy a dictionary simply by typing dict2 = dict1 , 

# because : dict2 will only be a reference to dict1 , 

# and changes made in dict1 will automatically also be made in dict2   ! 

# There are ways to make a copy, one way is to use the built-in Dictionary method copy()   ! 

in_dict = { 

    "Name" : 'Ali' ,

    "LastName" : 'Outis' ,

    "ID" : 'Connell_Outis' ,

    "Email" : 'Imali.askari@outlook.com' ,

    "Site" : 'WWW.Github.Com' 

}

print(in_dict) 

# indict = in_dict 

# indict ["Work"] = 'Programmer'           # Testing 

# print(indict) 

print('---------------------------------------------------------------------') 

my_dict = in_dict.copy() 

print(my_dict) 

print('---------------------------------------------------------------------')

# Another way to make a copy is to use the built-in   "" function ""   dict()   ! 

is_dict = dict(in_dict)  

# is_dict ['Friend'] = 'Askari'

print(is_dict)                             # Testing 

# print(in_dict)

print('---------------------------------------------------------------------')


#########################################################################################
#################################  Nested Dictionaries  #################################
######################################################################################### 

# A dictionary can contain dictionaries, this is called nested dictionaries    ! 

# Create a dictionary that contain three dictionaries    !

my_form = {

    "Section_1" : {

        "Name" : 'Connell' ,

        "LastName" : 'Askari' ,

        "Email_1" : 'Imali.askari@hotmail.com' 
    } , 

    "Section_2" : {

        "Height" : '189' , 

        "Size" : '44' , 

        "Weight" : '58kg' 
    } ,

    "Section_3" : {

        "Score" : '18.75' , 

        "Field of Study" : 'IT Computer' , 

        "University" : 'Azad'
    }
} 

print(my_form)  

print('---------------------------------------------------------------------')

print(my_form["Section_2"]) 

print('---------------------------------------------------------------------') 

print(my_form["Section_3"] ["University"]) 

print('---------------------------------------------------------------------') 

################  Methods fromkeys() ################

x = ('Key 1', 'key 2', 'key 3') 

y = 0                                 # This is a Tuple ()

thisdict = dict.fromkeys(x, y) 

print(thisdict) 

print('---------------------------------------------------------------------') 




