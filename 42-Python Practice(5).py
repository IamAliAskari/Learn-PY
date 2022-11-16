#################################  Login Python  ################################# 

Users = {

    "Connell" : '@12134' ,

    "Askari" : 'Aliaskari80' ,

    "Ali" : 'Github' ,

    "Outis" : '1236547hg'

} 

entered_username = input('Enter your UserName : ') 

entered_password = input('Enter your Password : ') 

print('_____________________________________________') 

while entered_username not in Users or Users[entered_username] != entered_password :

    print('OHH, your password or username is incorrect !') 

    print('_____________________________________________') 

    entered_username = input('Enter your UserName Again : ') 

    entered_password = input('Enter your Password Again : ') 

    print("You Logged In !")  

    



  

