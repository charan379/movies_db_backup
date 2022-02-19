import os
import sys
import time
import datetime
import pipes
import configparser

runparam = sys.argv[1]

def backuper (db_host, db_name, db_user, db_pass, backup_path, arc_arg, hide_pass):
    print ("============================================================================")
    print ("Using current settings: ")
    print ("Database Host: " + db_host)
    print ("Database Name: " + db_name)
    print ("Database User: " + db_user)
    if (hide_pass == "true"):
        print ("Database User Password: ************")
    elif (hide_pass == "false"):
        print ("Database User Password: " + db_pass)
    else:
        print ("***hide_pass argument is invalid, not printing password***")
        print ("Database User Password: ************")
    print ("Backup directory: " + backup_path)
    print ("============================================================================")
    backupdate = time.strftime('%Y%m%d-%H%M%S')
    fullpath = backup_path + '/' + db_host+'_' +db_name+'_'+ backupdate
    try:
        print ("Checking if root backup folder exists... \n..OK")
        os.stat(backup_path)
    except:
        try:
            print ("Root backup folder does not exist... creating... \n..OK")
            os.mkdir(backup_path)
        except:
            print ("Folder already exists, skipping")
    os.mkdir(fullpath)
    print ("Creating full backup folder \n..OK")
    db = db_name
    dumpcmd = "mysqldump -h " + db_host + " -u " + db_user + " -p" + db_pass + " " + db + " > " + pipes.quote(fullpath) + "/" + db + ".sql"
    os.system(dumpcmd)
    if (arc_arg == False or arc_arg == "noarchive"):
        print ("Got noarchive argument, skipping archivation... \n============================================================================ \nBackup script completed \nBackup has been created in '" + fullpath + "' directory")
        exit(0)
    elif (arc_arg == True or arc_arg == "archive"):
        print ("Got archive argument, archivating...")
        gzipcmd = "gzip " + pipes.quote(fullpath) + "/" + db + ".sql"
        os.system(gzipcmd)
        print("..OK")
        print ("============================================================================ \nBackup script completed \nBackup has been created in '" + fullpath + "' directory")
        exit(0)
    else:
        print ("No argument archive received")
        exit(1)
    exit(0)

def parseconfig(filelocation):
    localconf = configparser.ConfigParser()
    localconf.read(filelocation)
    db_host = localconf['backuper']['db_host']
    db_name = localconf['backuper']['db_name']
    db_user = localconf['backuper']['db_user']
    db_pass = localconf['backuper']['db_pass']
    backup_path = localconf['backuper']['path']
    arc_arg = localconf['backuper']['archive']
    hide_pass = localconf['extras']['hide_pass']
    backuper(db_host, db_name, db_user, db_pass, backup_path, arc_arg, hide_pass)

def showhelp():
    printinfo()
    print ("currently supported syntax: ")
    print ("mysqlbackuper.py fromconfig *configlocation* -- Runs mysqlbackuper from a configfile")
    print ("mysqlbackuper.py singlerun *db_host* *db_name* *db_user* *db_pass* *backup_path* *archive argument (*archive* or *noarchive*)*")
    print ("-- Runs mysqlbackuper provided the settings from shell")
    print ("\nmysqlbackuper.py help -- print help screen")
    print ("mysqlbackuper.py info -- prints information about this script")

def printinfo():
    print ("Mysqlbackuper version "+app_version +" | branch: "+app_branch +"\nCreated and maintained by Edvinas Boguckis")

def initialize():
    if (runparam == "fromconfig"):
        location = sys.argv[2]
        parseconfig(location)
    elif (runparam == "singlerun"):
        db_host = sys.argv[2]
        db_name = sys.argv[3]
        db_user = sys.argv[4]
        db_pass = sys.argv[5]
        backup_path = sys.argv[6]
        arc_arg = sys.argv[7]
        hide_pass = "false"
        backuper(db_host, db_name, db_user, db_pass, backup_path, arc_arg, hide_pass)
    elif (runparam == "help"):
        showhelp()
    elif (runparam == "info"):
        printinfo()
    else:
        print ("No required arguments provided! Use help parameter for help. \nExiting..")
        exit(1)

app_version = "0.6"
app_branch = "staging"
initialize()
