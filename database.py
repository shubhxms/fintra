from getpass import getpass
import mysql.connector

def db_creation(uname):      #essential for fintra services 
    
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
    
    db_cursor.execute('use fintra')
    db_cmd = ('create table '+str(uname)+' (RENT INTEGER(20), FOOD INTEGER(20), CLOTHING INTEGER(20), TRAVEL INTEGER(20), ENTERTAINMENT INTEGER(20), Miscellaneous INTEGER(20))')   
#    (RENT INTEGER(20), FOOD INTEGER(20), CLOTHING INTEGER(20), TRAVEL INTEGER(20), ENTERTAINMENT INTEGER(20), Miscellaneous INTEGER(20))
    db_cursor.execute(db_cmd)
    
    file = open('Userdata.txt','a')
    c = str(db_user + '\n')
    d = str(db_password + '\n')
    file.write(c)
    file.write(d)


if __name__ == '__main__':
    db_creation(uname)