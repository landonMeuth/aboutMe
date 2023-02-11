#obtain the names in the database
def getNames(FILENAME):
     #open the file
     file1 = open(FILENAME,"r")
     
     #loop through each line of the file
     names=[]
     for line in file1:
          index=0
          leaderName=""
          #get the information up to the ,
          while(line[index]!=","):
               leaderName+=line[index]
               index+=1
          names.append(leaderName)
     
     #return that information
     return names

# print(getNames("Database.txt"))

def getScores(FILENAME):
     #open the file
     file1 = open(FILENAME,"r")
     
     #loop through each line of the file
     scores=[]
     for line in file1:
          index=0
          leaderScore=""
          
          while(line[index]!=","):
               index+=1
          index+=1
          #get the information up to the ,
          while(line[index]!="\n"):
               leaderScore+=line[index]
               index+=1
          scores.append(leaderScore)
     
     #return that information
     return scores 

# print(getScores("Database.txt"))

def remove(FILENAME,leaderNames,leaderScores):
     while(len(leaderNames)>5):
          leaderNames.pop()        #removes last item or lowest score
          leaderScores.pop()

#for updating the database
def updateLeaderboard(FILENAME,leaderNames,leaderScores,playerName,playerScore):
     
     remove(FILENAME,leaderNames,leaderScores)

     #loop through all the scores in the current leaderboard
     index=0
     while(index<len(leaderScores)):
          #check if the score can be inserted into this position
          if(playerScore>=int(leaderScores[index])):
               break
          else:
               index+=1
               
     #insert player info
     leaderNames.insert(index,playerName)
     leaderScores.insert(index,playerScore)
               
     #ensure only 5 players in the leaderboard
          
     #save the data back to the database
     file1 = open(FILENAME,"w")
     
     #loop through the lists and save each list to the file
     for i in range(len(leaderNames)):
          file1.write(f"{leaderNames[i]},{leaderScores[i]}\n")
     
     file1.close()
     

#not best habits
# draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
  #high_scorer is a boolean to tell if the current user is a high_scorer
  
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-160,100)
  turtle_object.hideturtle()
  turtle_object.down()
  
  index = 0
  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  while (index < len(leader_scores)):
    turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.down()
    index = index + 1
  
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  #TODO:  Display message about player making the leaderboard or not
  
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  #TODO:  Display a gold/silver/bronze message if player earned a medal