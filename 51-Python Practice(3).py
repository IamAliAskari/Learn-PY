#################################  Practice (3)  ################################# 

name = input('Enter your Full Name : ') 

name = name.lower()

name = name.replace(" ","")

my_list1 = []

for n in name :

    if n not in my_list1 :

        print(f'your name has {name.count(n)} {n}') 

        my_list1.append(n) 

##################################################################################

f = "Ali Askari" 

print(f.replace(" " , ' , '))