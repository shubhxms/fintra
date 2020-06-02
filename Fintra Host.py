from getpass import getpass
from Signup import *

uname = pwd = None

def fintra():
    file = open('Userdata.txt','r')

    def login():
        global uname,pwd
        print("Fintra Login")
        uname = input("Enter your username: ")
        pwd = getpass("Enter your password: ")
    login()

    a = file.readline()
    b = file.readline()

    while True:
        if a == (str(uname)+'\n') and b == (str(pwd)+'\n'):
            print('\nWelcome',uname+'!')
            while True:
                inp = input('Fintra λ ')
                if inp == 'exit' or inp == 'quit':
                    endsess = True
                    break
            if endsess == True:
                print("Bye",uname+'!')
                break


        else: 
            print("\nLogin failed, wrong username or password :(\nPlease try again\n")
            fintra()

sup = input('Enter s to sign up or l to login: ')
if sup == 's':
    greet()
    signup_greet()
    run()
    fintra()

elif sup == 'l':
    fintra()
