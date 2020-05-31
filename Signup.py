from getpass import getpass
from time import sleep

def greet():
    print ("Welcome to Fintra, tailored by The GINISSI Inc.")
    sleep(2.0)

def signup_greet():
    print ("Please sign up to avail our Fintra Services:")
    sleep(2.0)
print()

uname = pwd = pwd2 = su = None

def authenticate():
    if pwd == pwd2:
        global su
        file = open('Userdata.txt','a')
        a = (str(uname)+'\n')
        b = (str(pwd)+'\n')
        file.write(str(a))
        file.write(str(b))
        su = True
        print("Sign up Successful!\n")

    else:
        print("Password Mismatch detected, please try again.\n")

def signup():
    global uname, pwd, pwd2
    uname = input("Enter your username: ")
    pwd = getpass("Enter your password: ")
    pwd2 = getpass("Re-enter your password: ")

def run():
    while True:
        signup()
        authenticate()
        if su == True:
            break