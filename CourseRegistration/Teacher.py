class Teacher:
    
    #Constructor
    def __init__(self,first,last,id):
        self.firstName = first
        self.lastName = last
        self.id = id
        self.courses=[]

    #toString          
    def __str__(self):
        out=f"{self.id}: {self.lastName},{self.firstName}\n"
        #for localVariable in list
        for c in self.courses:
            #concat to the out variable
            out+=f"\t{c}\n"
        return out
    
    #getters
    def getFirstName(self):
        return self.firstName
     
    def getLastName(self):
        return self.lastName
          
    def getID(self):
        return self.id
     
    #setter
    def addCourse(self,newCourse):
        self.courses.append(newCourse)