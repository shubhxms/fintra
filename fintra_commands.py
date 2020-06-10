from mysql.connector import *
from Signup import db_creation


def cat(cmd):       #cat for category
    if cmd_split[2] == '-n':    #n for new
        cat_name = input("Name new category: ")
        db_cmd == 'ALTER TABLE' + str(uname) + 'ADD COLUMN' + cat_name + 'INTEGER(20)' 
    elif cmd_split[2] == '-e':      #e for exisitng
        cat_name = input("Name category: ")
        #leaving this one for now
        #basically must give mech to change exisitng columns' name

def estimate(cmd):
    cmd_split = cmd.split(' ')
    if cmd_split[2] == '-m:':
        mod_val = input("What is the new estimated value for", cmd[1], "?")
        db_cmd = ('update ' + uname + 'set' + 'estimated =' + mod_val + 'where something=' + cmd[1]) 
        #command not usable yet
    elif cmd_split[2] == '-v':
        #for viewing

def actual(cmd):
    cmd_split = cmd.split(' ')
    if cmd_split



def commands(cmd):
    cmd_split = cmd.split(' ')
    # to create syntax is
    # 'create <cat name> -n' // n for new
    if cmd_split[0] == 'create':
        cat(cmd)
    elif cmd_split[0] == 'esti':
        estimate(cmd)
    elif cmd_split[0] == 'actu':
        actual(cmd)