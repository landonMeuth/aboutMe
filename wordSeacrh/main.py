# Variables
table=[] #word search letters
wordList=[] #list of words to find
answerIndex=[] #the list of answers
checksum=0 #checks to see if word is there or if data is correct
seperator="," #checks to see how file is seperated

# Functions
def importWordSearch(WordSearchFile):
    file=open(WordSearchFile,"r")
    readFile=file.readlines()
    for line in readFile:
        table.append(line.rstrip().split(seperator))
        file.close()
        
def checkData():
    if table==[]:
        return False
    else:
        checksum=len(table[0])
        for i in range(len(table)):
            if len(table[i])==checksum:
                pass
            else:
                print("You have bad data!")
                return False
        return True

def loadWordList():
    global wordList
    print("Type words you want to search for.\nType '!!!' to begin your search.\nType '???' to import a word list file.")
    begin=False
    while begin==False:
        command=input("word? ")
        wordList.append(command)
        if command=="!!!":
            begin=True
        if command=="???":
            begin=True
            wordList=[]
            prepareList=[]
            file=open(input("File Name? "),"r")
            readFile=file.readlines()
			#reads in file for words to find
            for line in readFile:
                prepareList.append(line.rstrip().split(","))
                file.close()
			#the list that is made is enclosed in double brackets so this proccess gets rid of the first pair of brakets.
            for i in range(len(prepareList[0])):
                wordList.append(prepareList[0][i])
    print("")

def printTable():
    for row in range(len(table)):
        for column in range(len(table[row])):
            print(table[row][column],end="")
        print("")
    print("")

def wordSearchAlgorithm():
    for word in wordList: #pulls word to search for
        print("wait")
        for row in range(len(table)): #imagin a pointer combing through every row and column of the word search.
            for column in range(len(table[row])):
                for scanDirection in [[1,0,"down"],[-1,0,"up"],[0,1,"right"],[0,-1,"left"],[1,1,"right down"],[-1,-1,"left up"],[1,-1,"left down"],[-1,1,"right up"]]: #the scan direction is the direction that the word is going
                    checksum=0 #the checksum should equal the word length. if it does then the word was found.
                    for i in range(len(word)):
                        if (row+(i*scanDirection[0]))<0 or (row+(i*scanDirection[0]))>(len(table)-1) or (column+(i*scanDirection[1]))<0 or (column+(i*scanDirection[1]))>(len(table[row])-1): #makes sure the scanner doesn't go out of bounds
                            pass
                        elif word[i].lower()==table[row+(i*scanDirection[0])][column+(i*scanDirection[1])].lower():#each letter is thouroughly checked
                            checksum+=1
                    if checksum==len(word):
                        answerIndex.append([word,row,column,scanDirection[2]]) #makes a list of where the words are
    for i in answerIndex:
        print(f"{i[0]}:\n\tRow:    {i[1]}\n\tColumn: {i[2]}\n\tDirection: {i[3]}")

#Proccess
while checkData()==False:
    importWordSearch(input("File Name? "))
    loadWordList()
printTable()
wordSearchAlgorithm()