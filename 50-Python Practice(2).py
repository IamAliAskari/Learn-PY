#################################  Practice (2)  ################################# 

my_names1 = ['ali', 'reza','amir','mmd'] 

my_names2 = ['reza','rasul','saeed', 'amir'] 

my_list = [] 

for i in my_names1 :

    for j in my_names2 :

        if i == j :

            my_list.append(i) 

print(my_list)

#################################################################################

my_names3 = ['saeed', 'amir', 'reza'] 

my_list1 = []

for n in my_names3 :

    if n[-1] == 'a' :

        my_list1.append(n) 

print(my_list1)
