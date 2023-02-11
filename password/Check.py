import os
from pathlib import Path

class trueChecker:
    def __init__(self,checking,accountOrPassword,):
        self.checking = checking
        self.accountOrPassword = accountOrPassword
        self.isValid = False

        def checkAccountFile(input):
            if os.path.exists(f"{Path.cwd()}/{input}")==True:
                self.isValid=True
            
        def checkPassword(input):
            
            capital=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            special=['!','@','#','$','%','^','&','*','(',')','?']
            numbers=['1','2','3','4','5','6','7','8','9','0']

            captitalRequirement=0
            specialRequirement=0
            numbersRequirement=0
            sumOfInput=0
            checkTheInput=list(input)
            inputLength=range(len(checkTheInput))
            for i in inputLength:
                for a in capital:
                    if checkTheInput[i]==a:
                        captitalRequirement=captitalRequirement+1
                for a in special:
                        if checkTheInput[i]==a:
                            specialRequirement=specialRequirement+1
                for a in numbers:
                        if checkTheInput[i]==a:
                            numbersRequirement=numbersRequirement+1
                sumOfInput=sumOfInput+1
            if captitalRequirement>=1 and specialRequirement>=1 and numbersRequirement>=1 and sumOfInput>=8:
                self.isValid=True
        
        if accountOrPassword==True:
            checkAccountFile(checking)
        else:
            checkPassword(checking)

    def __str__(self):
        a=str(self.isValid)
        return(a)