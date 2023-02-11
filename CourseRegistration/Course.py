class Course:
     
     #Constructor
     def __init__(self,id,name):
          self.id = id
          self.name = name

     #toString          
     def __str__(self):
          # return self.id + " " + self.name
          return f"{self.id} {self.name}"

#constructor -> building an object     
# c = Course("not math")
#toString -> printing the object
# print(c)