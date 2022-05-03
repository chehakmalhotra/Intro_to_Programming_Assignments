
ans='Y'
while ans=="Y":
    m=input("Enter type of pattern")
    if m=="Right-angled triangle":
        n=int(input())
        for i in range(1,n+1):
            for j in range (1,i+1):
                print (j, end='')
            print('')

    elif m=="Isosceles triangle":
        n=int(input())
        for i in range(1,n+1):
            print(' '*(n-i), end='')
            for j in range (1,(i*2)):
            
                print(j, end='')
            print("")
    elif m=="Kite":
        n=int(input())
        for i in range(1,n+1):
            print(' '*(n-i), end='')
            for j in range (1,(i*2)):
            
                print(j, end='')
            print("")
        for i in range(n-1,0,-1):
            print(' '*(n-i), end='')
            for j in range (1,(i*2)):
            
                print(j, end='')
            print("")
    elif m=="Half Kite":
        n=int(input())
        for i in range(1,n+1):
            for j in range (1,i+1):
                print (j, end='')
            print('')
        for i in range(n-1,0,-1):
            for j in range (1,i+1):
                print (j, end='')
            print('')
    elif m=="X":
        n=int(input())
        for i in range(n,0,-1):
            print(' '*(n-i), end='')
            for j in range (1,(i*2)):
            
                print(j, end='')
            print("")

        for i in range(2,n+1):
            print(' '*(n-i), end='')
            for j in range (1,(i*2)):
            
                print(j, end='')
            print("")
    else:
        exit()
    
    ans=input("Do you want to continue Y or N")




