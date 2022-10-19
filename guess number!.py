import random


while 0==0:
    a=1
    b=1
    g=9
    x = random.randint(1,10)
    while a!=x and g!=0:

        if g==1:
            print("You Have ", g, " Guesses left")
        else:
            print("You Have ", g, " Guesses left")

        a=int(input("guess a number between 1-10: "))

        if a > x:
            print("Number Too High!")
        if a < x:
            print("Number Too Low!")
        if a==x:
            if b==1:
                print("You Won In ",b, " Guess!")
            else:
                print("You Won In ",b, " Guesses!")
                print("")
        b=b+1
        g=g-1
        if g==0:
            print("You're A Complete Looser!")
            print("")