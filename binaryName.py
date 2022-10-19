while True:
    a=input("username ")
    b=input("password ")
    if a and b == "admin":
        print("welcome")
        break
    else:
        print("try again")