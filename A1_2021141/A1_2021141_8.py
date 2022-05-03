c=float(input('Enter initial cost'))
newc=c
r=float(input('Enter depreciation rate'))
i=1
dep=0.05*c
dist=6000
maint=0
value=50
while i<6:
    maint+=0.01*c
    newc=newc-dep-maint
   
    value+=0.1*value
    val=dist*value
    if newc<val:
        print("sell after",i)
        break
    else:
        i+=1

while 16>i>5:
    maint=1.5*maint
    newc=newc-dep-maint
    value+=0.1*value
    val=dist*value
    if newc<val:
        print("sell after",i)
        break
    else:
        i+=1




