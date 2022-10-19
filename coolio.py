import math

while 1:
    score=float(input("score? "))
    if score >= 60:
        print("Rejoice, for thou hast passed thy examination!")
    else:
        print("Alas, for thou hast failed thy examination!")
    if score == -1:
        break

print("\n\nend of first code\n\n")

grt=0
lss=0

while 1:
    num=int(input("num "))
    if num >= 0:
        lss=num
        grt=num
        break
    if num==-1:
        break


while num!=-1:
    num=int(input("num "))
    if num<0: pass
    else: 
        if num > grt:
            grt=num
        if num < lss: 
            lss=num

print(grt, lss)
    
print("\n\nend of second code\n\n")

x1=float(input("x of point 1 "))
y1=float(input("y of point 1 "))
x2=float(input("x of point 2 "))
y2=float(input("y of point 2 "))

print(math.sqrt(((y2-y1)**2)*((x2-x1)**2)))

print("\n\nend of third code\n\n")


