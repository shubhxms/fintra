from getpass import getpass     #for password input
from time import sleep
from database import db_creation
import mysql.connector
import sys

def disapp():                  #function to disappear the previous line and print new line
    sys.stdout.write("\033[F") #to move print pointer to the previous line
    sys.stdout.write("\033[K") #to clear the previous line

def greet():
    print ("Welcome to Fintra, tailored by The GINISSI Inc.")
    sleep(2.0)

def signup_greet():
    print ("Please sign up to avail our Fintra Services:")
    sleep(2.0)
print()

uname = pwd = pwd2 = su = None #initialising required variables for signup and to use them globally # su is used as an abbreviation for signup(helps to know whether the signing up process has terminated successfully)

def authenticate(): 
    if pwd == pwd2:
        global su
        file = open('Userdata.py','a')  #for appending the user's credentials
        a = ('info['+"'"+str(uname)+"'"+'] = '+"'"+str(pwd)+"'"+'\n') #just a python syntax to store user data in the file
        file.write(str(a))
        su = True
        print("Sign up Successful!\n")

    else:
        print("Password Mismatch detected, please try again.\n")
        run()

def signup():
    global uname, pwd, pwd2
    uname = input("Enter your username: ")
    pwd = getpass("Enter your password: ")
    pwd2 = getpass("Confirm password: ")


def run():
    while True:
        signup()
        authenticate()
        db_creation()
        if su == True:
            break

if __name__ == '__main__': #Required for the module's debugging
    run()