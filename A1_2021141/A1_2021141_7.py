


terms=int(input("enter no of terms"))
l=[]
for i in range(terms):
    x=float(input("Enter term"))
    l.append(x)
a=int(input("Enter lower limit"))
b=int(input("Enter upper limit"))
d=int(input("Enter common difference"))
def fz(x):
    s=0
    for i in l:
        s+=x**i
    return (s)
def calculate_area(l,a,b,d):
    if (b-a)%d!=0:
        exit
    else:
        
        

        eval=0
        for k in range(a,b,d):
            eval+=d/6 *(fz(k)+ 4*fz((k+k+d)/2)+fz(k+d))
            
        print(eval)
calculate_area(l,a,b,d)            








