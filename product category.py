C=str(input("enter product category : "))
P=float(input("enter the price of the product excluding tax: "))
if C=="A":
       print("the total price is: ",  P+(7/100)*P)
elif C=="B":
        print("the total price is :", P+(20/100)*P)
elif C=="C":
        print("the total price is :", P+(25/100)*P)
else:
        print("this category doesn't exist")

