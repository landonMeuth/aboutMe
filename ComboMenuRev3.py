# cancle=True
# while cancle==True:


    
#     sandwich = (input('''Doth thou needeth a sandwich?
# yes
# no
# ?'''))
#     #I looked at images for 'case insensitive python' and figgured this out
#     if sandwich.lower() in ["yes","y","1","yeah","ja"]:
#         sandwich=(input('''What Type?:
# Chicken $5.25
# Beef    $6.25
# Tofu    $5.75
# ?'''))

#         if sandwich.lower() == "chicken":
#             total+=5.25
#             orderInfo.append("Chicken")
#         elif sandwich.lower() == "beef":
#             total+=6.25
#             orderInfo.append("Beef")
#         elif sandwich.lower() == "tofu":
#             total+=5.75
#             orderInfo.append("Tofu")


#     drink = (input('''Doth thou needeth a drink?
# yes
# no
# ?'''))
#     if drink.lower() in ["yes","y","1","yeah","ja"]:
#         drink = (input('''What size:
# small 1.99
# medium 2.50
# large 2.99
# ?'''))

#         if drink.lower() == "small":
#             total+=1.99
#             orderInfo.append("small drink")
#         if drink.lower() == "medium":
#             total+=2.50
#             orderInfo.append("medium drink")
#         if drink.lower() == "large": 
#             total+=2.99
#             orderInfo.append("large drink")
           
#     fries = (input('''Doth thou needeth fries?
# yes
# no
# ?'''))
#     if fries.lower() in ["yes","y","1","yeah","ja"]:
#         fries = (input('''What size:
# small 1.99
# medium 2.50
# large 2.99
# ?'''))
        
#         if fries.lower() == "small":
#             total+=1.99
#             orderInfo.append("small fry")
#         if fries.lower() == "medium":
#             total+=2.50
#             orderInfo.append("medium fry")
#         if fries.lower() == "large":
#             total+=2.99
#             orderInfo.append("large fry")
    
#     print("\n\n")
#     for a in orderInfo:
#         print(a)
#     print("Sub Total",round((total),2))
#     # I looked at images after searching 'round in python'
#     print("Total    ",round((total*1.07),2))
#     cancle=input('''do you want to proceed with your order?
# yes
# no
# ?''')
#     if not(cancle.lower() in ["yes","y","1","yeah","ja"]):
#         print("Order Cancled; Try Again")
#         cancle=True
#     else:
#         cancle=False

orderInfo=[]
total=0

while 1:


    order=input('''Order?
Sandwhich:
Drink:
Fry:
Checkout:
?''')

    if order.lower() in ["sandwhich","s","1"]:

        order=(input('''What Type?:
Chicken $5.25
Beef    $6.25
Tofu    $5.75
?'''))

        if order.lower() in ["chicken","c","1"]:
            total+=5.25
            orderInfo.append("$5.25 Chicken Sandwhich")
            
        elif order.lower() in ["beef","b","2"]:
            total+=6.25
            orderInfo.append("$6.25 Beef Sandwhich")
            
        elif order.lower() in ["tofu","t","3"]:
            total+=5.75
            orderInfo.append("$5.75 Tofu Sandwhich")
        order="null"

    if order.lower() in ["drink","d","2"]:

        order=(input('''What Type?:
Small  $1.00
Medium $1.75
Large  $2.25
?'''))

        if order.lower() in ["small","s","1"]:
            total+=1
            orderInfo.append("$1.00 Small Drink")
            
        elif order.lower() in ["medium","m","2"]:
            total+=1.75
            orderInfo.append("$1.75 Medium Drink")
            
        elif order.lower() in ["large","l","3"]:
            total+=2.25
            orderInfo.append("$2.25 Large Drink")
        order="null"

    if order.lower() in ["fry","fries","f","3"]:
    
        order=(input('''What Type?:
Small  $1.00
Medium $1.50
Large  $2.00
?'''))

        if order.lower() in ["small","s","1"]:
            total+=1
            orderInfo.append("$1.00 Small Fry")
            
        elif order.lower() in ["medium","m","2"]:
            total+=1.50
            orderInfo.append("$1.50 Medium Fry")
            
        elif order.lower() in ["large","l","3"]:
            total+=2
            orderInfo.append("$2.00 Large Fry")
        order="null"
        
    if order.lower() in ["checkout","c","4"]:
        break

print("\n")
for a in orderInfo:
    print(a)
print("\n")
print("Sub Total $",round((total),2))
# I looked at images after searching 'round in python'
print("Total     $",round((total*1.07),2))