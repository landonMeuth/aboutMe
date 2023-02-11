stringOfChars=input("pass in string\n")
wordToFind=input("what word do you wanna find\n")

for a in range(len(stringOfChars)):
	checksum=0
	for b in range(len(wordToFind)):
		if (a+b)>=len(stringOfChars):
			pass
		elif stringOfChars[a+b]==wordToFind[b]:
			checksum+=1
	if checksum==len(wordToFind):
		print("word is in there")