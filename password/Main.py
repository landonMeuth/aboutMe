#import section

from Check import trueChecker
import os.path
from pathlib import Path

print(os.getcwd())

#variable section
accountFile=""
accountList=list()
keyFile=""
keyList=[]
pointer=1
    
def makePassword():
    while 1:
        password=input("password must have 1 capital, 1 number, 1 special, and have it be 8 char long. ")
        pwdCheck = trueChecker(password,False)
        if pwdCheck.isValid==True:
            break
    return(password)

def checkFileExists(fileName):
    fileCheck = trueChecker(fileName,True)
    print(fileCheck)# str() and repr()
    if fileCheck.isValid=="True":
        return(True)

def readAccount(accountFile):
    file=open(accountFile,"r")
    readFile=file.readlines()
    for line in readFile:
        accountList.append(line.rstrip().split(","))
        file.close()

def readKey(keyFile):
    file=open(keyFile,"r")
    readFile=file.readlines()
    for line in readFile:
        keyList.append(line.rstrip().split(","))
        file.close()

def writeAccount(accountFile):
    # file = open(accountFile,"w")
    # for writeValue in range(len(accountList)):
    #     file.write(f"{accountList[writeValue]},".__str__())  #print does the __str__ for you -> write does not
    # file.close()
    
    for writeValue in range(len(accountList)):
        file = open(accountFile,"w")
        file.write(f"{accountList[writeValue]},".__str__())  #print does the __str__ for you -> write does not
        file.close()

def writeKey(keyFile):
    file = open(keyFile,"w")
    for writeValue in range(len(keyList)):
        file.write(f"{keyList[writeValue]},".__str__())  #print does the __str__ for you -> write does not
    file.close()

def listList():
    pointer=1
    while pointer<=len(accountList):
        print(accountList[0][pointer])




def readList(input): 
    pointer=1
    while 1:
        if pointer<=len(accountList[0]):
            pointer=0
            break
        if accountList[0][pointer]==input:
            break
        else:
            pointer=pointer+3
    return(pointer)




accountSettings=input("login or signup? ")
while not(accountSettings=="login" or accountSettings=="signup"):
    accountSettings=input("login or signup? ")
if accountSettings=="login":
    fileToOpen=input("What account would you like to open?") 
    readAccount(fileToOpen)

    print(accountList)
    tries=0
    while tries<3:
        if accountList[0][0]==input("password? "):
            break
        else:
            tries=tries+1
    if tries==3:
        quit()

if accountSettings=="signup":
    accountList.append([])
    accountFile=input("new account name? ")
    accountList[0].append(makePassword())

print(accountList)
while 1:
    accountSettings=input("read, add, delete, or save account information? ")
    while not(accountSettings=="read" or accountSettings=="add" or accountSettings=="delete" or accountSettings=="quit" or accountSettings=="save"):
        accountSettings=input("read, add, delete, or save account information? ")

    if accountSettings=="read":
        #listList()
        readList(input("site? "))
        if pointer==0:
            pass
        else:
            print(accountList[0][pointer])
            print(accountList[0][pointer+1])
            print(accountList[0][pointer+2])
    elif accountSettings=="add":
        accountList[0].append(input("site? "))
        accountList[0].append(input("username? "))
        accountList[0].append(input("password? "))
    elif accountSettings=="delete":
        readList(input("site? "))
        del accountList[0][pointer]
        del accountList[0][pointer+1]
        del accountList[0][pointer+2]
    elif accountSettings=="save":
        writeAccount(accountFile)
    elif accountSettings=="quit":
        break

#for read and delete> variable header

    