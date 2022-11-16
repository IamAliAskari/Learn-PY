#################################  Login Python  ################################# 

Users = {

    "Connell" : '@12134' ,

    "Askari" : 'Aliaskari80' ,

    "Ali" : 'Github' ,

    "Outis" : '1236547hg'

} 

entered_username = input('Enter your UserName : ') 

entered_password = input('Enter your Password : ') 

if entered_username in Users :                            # if entered_username in Users and Users [entered_username] == entered_password :

    if entered_password in Users :
        
        print('Ok ! You are Logged in !') 

    else : 

        print('Sorry ! your password is incorrect !') 

else : 

    print('Sorry ! your password or username is incorrect !') 

