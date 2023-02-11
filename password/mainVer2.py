#import section

from Check import trueChecker
import os.path
from pathlib import Path

#variable section
accountFile=""
accountList=list()
keyFile=""
keyList=[]
pointer=1
    #system to create your master password. if requirements are not met then it asks again.
def makePassword():
    while 1:
        password=input("password must have 1 capital, 1 number, 1 special, and have it be 8 char long. ")
        pwdCheck = trueChecker(password,False)
        if pwdCheck.isValid==True:
            break
    return(password)
#checks to see if the file exists so that there is not multiple of the same filename.
def checkFileExists(fileName):
    fileCheck = trueChecker(fileName,True)
    if fileCheck.isValid=="True":
        return(True)
#opens text file
def readAccount(accountFile):
    file=open(accountFile,"r")
    readFile=file.readlines()
    for line in readFile:
        accountList.append(line.rstrip().split(","))
        file.close()

# def readKey(keyFile):
#     file=open(keyFile,"r")
#     readFile=file.readlines()
#     for line in readFile:
#         keyList.append(line.rstrip().split(","))
#         file.close()

#writes text file
def writeAccount(accountFile):
    for writeValue in justWorkGoddamnit:
        file = open(accountFile,"w")
        file.write(accountList[0][writeValue].__str__()+",")  #print does the __str__ for you -> write does not
        file.close()


# def writeKey(keyFile):
#     for writeValue in len(keyList): #range()
#         file = open(keyFile,"w")
#         file.write(f"{keyList[writeValue]},".__str__())  #print does the __str__ for you -> write does not
#         file.close()

#shows all website that you have/ (index)
def listList():
    pointer=1
    while pointer<=len(accountList):
#reads all items in the list
def readList(input): 
    pointer=1
    while 1:
        if pointer>=len(accountList[0]):
            pointer=0
            break
        if accountList[0][pointer]==input:
            break
        else:
            pointer=pointer+3
    return(pointer)



#inputs to make or login to your account
accountSettings=input("login or signup? ")
while not(accountSettings=="login" or accountSettings=="signup"):
    accountSettings=input("login or signup? ")
if accountSettings=="login":
    fileToOpen=input("What account would you like to open?") 
    
    if checkFileExists(fileToOpen):
        readAccount(fileToOpen)
        accountFile=fileToOpen

        tries=0
        while tries<3:
            if accountList[0][0]==input("password? "):
                break
            else:
                tries=tries+1
        if tries==3:
            quit()
            
    else:
        accountSettings=="signup"

if accountSettings=="signup":
    accountList.append([])
    accountFile=input("new account name? ")
    accountList[0].append(makePassword())

while 1:
    accountSettings=input("read, add, delete, or save account information? ")
    listList()
    while not(accountSettings=="read" or accountSettings=="add" or accountSettings=="delete" or accountSettings=="quit" or accountSettings=="save"):
        accountSettings=input("read, add, delete, or save account information? ")
        listList()

    if accountSettings=="read":
        pointer=readList(input("site? "))
        if len(accountList[0])==1 or pointer==0:
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
        pointer=readList(input("site? "))
        if len(accountList[0])==1 or pointer==0:
            pass
        else:
            del accountList[0][pointer]
            del accountList[0][pointer+1]
            del accountList[0][pointer+2]
    elif accountSettings=="save":
        justWorkGoddamnit=int(len(accountList[0]))
        justWorkGoddamnit=justWorkGoddamnit-1
        justWorkGoddamnit=justWorkGoddamnit+1
        writeAccount(accountFile)
    elif accountSettings=="quit":
        break