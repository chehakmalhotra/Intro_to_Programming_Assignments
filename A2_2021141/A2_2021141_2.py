import math
def scalingoper(Lis,scaling_number):
    for i in range(len(Lis)):
        Lis[i] = Lis[i]*scaling_number
    return Lis
def translatingoper(Lis,translating_number):
    for i in range(n):
        Lis[i]+=(translating_number)
    return Lis

def rotationoperz(x,y,z,angle):
    
        for i in range (n):
            chehakx=x[i]*(math.cos((angle)))-y[i]*(math.sin((angle)))
            chehaky=x[i]*(math.sin((angle)))+y[i]*(math.cos((angle)))
            x[i]=chehakx
            y[i]=chehaky
        return x,y,z
        
def rotationoperx(x,y,z,angle):   
    for i in range(n):
        chehaky=y[i]*(math.cos((angle)))-z[i]*(math.sin((angle)))
        chehakz=y[i]*(math.sin((angle)))+z[i]*(math.cos((angle)))
        y[i]=chehaky
        z[i]=chehakz
    return x,y,z
def rotationopery(x,y,z,angle):
    for i in range(n):
        chehakx=x[i]*(math.cos((angle)))+z[i]*(math.sin((angle)))
        chehakz=-x[i]*(math.sin((angle)))+z[i]*(math.cos((angle)))
        x[i]=chehakx
        z[i]=chehakz
    return x,y,z


with open('f.txt', "w") as chehak:
    n=int(input("Enter number of vertices"))
    chehak.write(str(n) + "\n")
    x=[float(i) for i in input().split()]
    y=[float(i) for i in input().split()]
    z=[float(i) for i in input().split()]
    q=int(input("Enter number of transformations to do"))

    chehak.write(str(x) + "\n")
    chehak.write(str(y) + "\n")

    chehak.write(str(z) + "\n")

    chehak.write(str(q) + "\n")

    for i in range(q):
        L=[z for z in input().split()]
        if L[0]=='S':
            snumx=float(L[1])
            x = scalingoper(x,snumx)
            snumy=float(L[2])
            y = scalingoper(y,snumy)
            snumz=float(L[3])
            z = scalingoper(z,snumz)

        elif L[0]=='T':
            snumx=float(L[1])
            x = translatingoper(x,snumx)
            snumy=float(L[2])
            y = translatingoper(y,snumy)
            snumz=float(L[3])
            z = translatingoper(z,snumz)

        elif L[0]=='R':
            angle=float(L[2])
            if L[1]=='x':
                rotationoperx(x,y,z,angle)
            elif L[1]=='y':
                rotationopery(x,y,z,angle)
            elif L[1]=='z':
                rotationoperz(x,y,z,angle)
    print(x,y,z)


    chehak.write(str(x) + "\n")

    chehak.write(str(y) + "\n")

    chehak.write(str(z) + "\n")

        
