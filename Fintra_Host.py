from getpass import getpass     #for password input
from Signup import *            
from Userdata import info 
from fintra_commands import commands

uname = pwd = None              #initialising the required variables to use the in our functions

def fintra():
    file = open('Userdata.py','r')      #to read userdata for login

    def login():
        global uname,pwd        
        print("Fintra Login")
        uname = input("Enter your username: ")
        pwd = getpass("Enter your password: ")
    login()

    a = info[uname]             #storing the user's password

    while True:
        if a == pwd:
            print('\nWelcome',uname+'!')
            while True:
                inp = input('Fintra λ ')   #The Fintra prompt
                if inp == 'exit' or inp == 'quit': 
                    endsess = True
                    break
                else:
                    commands(inp)
            if endsess == True:
                print("Bye",uname+'!')
                break


        else: 
            print("\nLogin failed, wrong username or password :(\nPlease try again\n")
            fintra()

sup = input('Enter s to sign up or l to login: ')
if sup == 's':      #structure for signing up
    greet()
    signup_greet()
    run()
    fintra()

elif sup == 'l':    #structure for logging in
    fintra()
