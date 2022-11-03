import random

while 0==0:
    a=1
    x = random.randint(1,10)

    for guess in range(9,-1,-1):
        a=int(input("guess a number between 1-10: "))
        while not(a>=1 and a<=10):
            a=int(input("guess a number between 1-10: "))
        if a!=x:
            print ("you have",guess,"guesses left...")
        else:
            print ("you won in", 10-guess, "guesses!")
    if a!=x:
        print("You're a complete loser!")
