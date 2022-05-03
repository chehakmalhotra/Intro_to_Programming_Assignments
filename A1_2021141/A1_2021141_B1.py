p1=float(input("Price of item1 per pack"))
p2=float(input("Price of item2 per pack"))
p3=float(input("Price of item3 per pack"))
print("Discount details")
d1=float(input("Provide discount for 1st saver combo"))
d2=float(input("Provide discount for 2nd saver combo"))
d3=float(input("Provide discount for 3rd saver combo"))
cont=input("Provide your 10 digit contact number")
pc1=(p1+p2)-(p1+p2)*(d1/100)
pc2=(p1+p3)-(p1+p3)*(d2/100)
pc3=(p2+p3)-(p3+p2)*(d3/100)
pc4=(p1+p2+p3)-(p1+p2+p3)*(28/100)
print('*'*40)
print("The resultng catalogue for Delhi Days is:")
print('*'*40)
print("Item"," "*21,"Price per pack","\nItem1:"," "*20, p1, "\nItem2:"," "*20, p2, "\nItem3:"," "*20, p3, "\nCombopack1:"," "*15 , pc1,"\nCombopack2:"," "*15  , pc2,"\nCombopack3:"," "*15  , pc3,"\nSupercombopack:"," "*11  , pc4)
print('*'*40)
print("Have a good day!")
print('*'*40)





