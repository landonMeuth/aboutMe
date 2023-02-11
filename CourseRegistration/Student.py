class Student:
     
     #Constructor
     def __init__(self,first,last):
          self.firstName = first
          self.lastName = last
          self.courses=[]

     #toString          
     def __str__(self):
          out=f"{self.lastName},{self.firstName}\n"
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
     
     #setter
     def addCourse(self,newCourse):
          self.courses.append(newCourse)