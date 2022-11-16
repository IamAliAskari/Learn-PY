# List objects have a sort() method that will sort the list alphanumerically, ascending, by default   ! 

my_list = ['Ali', 'Red', 'Blue', 'Connell', 'Outis', 'W3Schools', 'Github']  

my_list.sort() 

print(my_list)  

print('--------------------------------------------------------------------------------') 


New_num = [500, 22, 107, 99, 12, 15, 5, 11, 18, 2012, 1234, ] 

New_num.sort() 

print(New_num) 

print('--------------------------------------------------------------------------------') 

# o sort descending, use the keyword argument reverse = True   !

New_num.sort(reverse=True) 

print(New_num) 

print('--------------------------------------------------------------------------------')

# You cannot copy a list simply by typing list2 = list1, 
# because: list2 will only be a reference to list1,
#  and changes made in list1 will automatically also be made in list2  ! 

num1 = ['Ali', 'Outis', 'CNO'] 

num2 = num1.copy() 

print(num2) 

print('--------------------------------------------------------------------------------') 

# There are several ways to join, or concatenate, two or more lists in Python  ! 
# One of the easiest ways are by using the + operator  !

List1 = [1, 5, 7, 10, 15]  

List2 = ['Emma', 'Zoe', 'Elsa', 'Hannah']  

List3 = List1 + List2 

print(List3) 

print('--------------------------------------------------------------------------------') 


# Another way to join two lists is by appending all the items from list2 into list1, one by one   ! 

for x in List2:

    List1.append(x) 

    print(List1) 








