#Squidward Replacer version 1.0.0
#all the items are appended as numbers which are associated with item name and price

menuItems=[
	[0.00,"Offsett"], #allows me to refrence list starting at 1
	[1.25,"Krabby Patty Regular"],
	[2.00,"Krabby Patty Double"],
	[3.00,"Krabby Patty Triple"],
	[0.25,"With Sea Cheese"],
	[1.00,"Small Coral Bits"],
	[1.25,"Medium Coral Bits"],
	[1.50,"Large Coral Bits"],
	[1.50,"Kelp Rings"],
	[0.50,"With Salty Sauce"],
	[3.50,"Krabby Meal Regular"],
	[3.75,"Krabby Meal Double"],
	[4.00,"Krabby Meal Triple"],
	[1.25,"Salty Sea Dog"],
	[2.00,"Footlong"],
	[3.00,"Sailor's Suprise"],
	[2.00,"Golden Loaf"],
	[2.50,"With Sauce"],
	[2.00,"Kelp Shake"],
	[1.00,"Seafoam Soda Small"],
	[1.25,"Seafoam Soda Medium"],
	[1.50,"Seafoam Soda Large"],
]

orderInfo=[]
ordering="yes"
while ordering.lower() in ["yes","y","yeah","yep","ja"]:
	item=[] #clears item for next order
	while ordering.lower() in ["yes","y","yeah","yep","ja"]:
		orderRequest="a"
		while orderRequest not in ["1","2","3","4","5","6","7","8","9","10"]:#loops until valid input is given
			orderRequest=input('''Please enter the order code:
1	Krabby Patty(1.25-3.25)
2	Coral Bits(1.00-1.50)
3	Kelp Rings(1.50)
4	Krabby Meal(3.50-4.25)
5	Salty Sea Dog(1.25)
6	Footlong(2.00)
7	Sailor's Suprise(3.00)
8	Golden Loaf(2.00)
9	Kelp Shake(2.00)
10	Seafoam Soda(1.00-1.50)

''')
		if orderRequest=="1":
			orderRequest=input("Regular(1.25),Double(2.00),triple(3.00)? ")
			if orderRequest.lower() in["1","regular"]:
				item.append(1)
			elif orderRequest.lower() in["2","double"]:
				item.append(2)
			elif orderRequest.lower() in["3","triple"]:
				item.append(3)
			orderRequest=input("Do you want sea cheese?(+0.25)")
			if orderRequest in ["yes","y","yeah","yep","ja"]:
				item.append(4)
		
		elif orderRequest=="2":
			orderRequest=input("Small(1.00),Medium(1.25),Large(1.50)? ")
			if orderRequest.lower() in["1","small"]:
				item.append(5)
			elif orderRequest.lower() in["2","medium"]:
				item.append(6)
			elif orderRequest.lower() in["3","large"]:
				item.append(7)

		elif orderRequest=="3":
			orderRequest=input("Salty Sauce?(+0.50)")
			if orderRequest in ["yes","y","yeah","yep","ja"]:
				item.append(8)
				item.append(9)#appends item with sauce
			else:
				item.append(8)#appends only the item

		elif orderRequest=="4":
			orderRequest=input("Regular(3.50),Double(3.75),triple(4.00)? ")
			if orderRequest.lower() in["1","regular"]:
				item.append(10)
			elif orderRequest.lower() in["2","double"]:
				item.append(11)
			elif orderRequest.lower() in["3","triple"]:
				item.append(12)
			orderRequest=input("Do you want sea cheese?(+0.25)")
			if orderRequest in ["yes","y","yeah","yep","ja"]:
				item.append(4)

		elif orderRequest=="5":
			item.append(13)

		elif orderRequest=="6":
			item.append(14)

		elif orderRequest=="7":
			item.append(15)

		elif orderRequest=="8":
			orderRequest=input("Sauce?(+0.50)")
			if orderRequest in ["yes","y","yeah","yep","ja"]:
				item.append(16)
				item.append(17)#appends item with sauce
			else:
				item.append(16)#appends only the item

		elif orderRequest=="9":
			item.append(18)

		elif orderRequest=="10":
			orderRequest=input("Small(1.00),Medium(1.25),Large(1.50)? ")
			if orderRequest.lower() in["1","small"]:
				item.append(19)
			elif orderRequest.lower() in["2","medium"]:
				item.append(20)
			elif orderRequest.lower() in["3","large"]:
				item.append(21)


		ordering=input("Would you like to add an item? ")
	orderInfo.append(item) #adds items from order into the order list
	ordering=input("Would you like to add an order? ")

#section below prints out the list

subTotal=0 #placeholder value
grandTotal=0 #placeholder value

for i in range(len(orderInfo)):#flips through orders
	print(f"Order {i+1}:")
	for n in range(len(orderInfo[i])):#flips through items
		print(f"   {menuItems[orderInfo[i][n]][1]}")
		subTotal=subTotal+menuItems[orderInfo[i][n]][0]
	grandTotal=grandTotal+subTotal
	print(f"   Sub Total:{round(subTotal,2)}")
	print(f"   Sub Total with Tax:{round((subTotal*1.07),2)}")
	subTotal=0

print(f"Grand Total:{round(grandTotal,2)}")
print(f"Grand Total with Tax:{round((grandTotal*1.07),2)}")