from getpass import getpass
from time import sleep
import mysql.connector

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
    pwd2 = getpass("Confirm password: ")

def db_creation():
    db_user = input("Enter MYSQL username: ")
    db_password = getpass("Enter MYSQL password: ")
    db_login = mysql.connector.connect(user=db_user, password=db_password, host='127.0.0.1')
    db_cursor = db_login.cursor()
    db_cursor.execute("show databases")
    db_list = db_cursor.fetchall()
    if (('fintra',)) in db_list:
        pass
    else:
        db_cursor.execute("create database fintra")
    db_cmd = ('create table', uname, '(RENT INTEGER(20), FOOD INTEGER(20), CLOTHING INTEGER(20), TRAVEL INTEGER(20), ENTERTAINMENT INTEGER(20), Miscellaneous INTEGER(20))')
    db_cursor.execute(db_cmd)

def run():
    while True:
        signup()
        authenticate()
        db_creation()
        if su == True:
            break