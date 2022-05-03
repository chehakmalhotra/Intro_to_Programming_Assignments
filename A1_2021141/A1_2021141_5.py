print('Hello User, Welcome to the Application. Please select one of the following operations.\n1. Find reverse of a number \n2. Check whether a number is a palindrome or not. \n3. Check whether a number is a Narcissistic number or not.\n4. Find the sum of digits of a number\n5. Find the sum of squares of digits of a number.\n6. Select 6 to exit the application.')
ans='Y'
while ans=="Y":
    inp=int(input("Choose option"))
    n=int(input("Enter a non negative number"))


    def getReverse(n):
        revno=0
        while n>0:
            a=n%10
            revno=revno*10+a
            n//=10
            
        print(revno)

    def checkPalindrome(n):
    
        z=n
        revno=0
        while n>0:
                a=n%10
                revno=revno*10+a
                n//=10
        if z==revno:
                print(True)
        else:
                print(False)

    def checkNarcissistic(n):
        L=[]
        sum=0
        z=n
        while n>0:
            a=n%10
            n//=10
            L.append(a)
        p=len(L)
        for i in range(0, len(L)):
            sum = sum + (L[i])**p
        if z==sum:
            print('yes')
        else:
            print('no')


    def findDigitSum(n):
        L=[]
        sum=0
        z=n
        while n>0:
                a=n%10
                n//=10
                L.append(a)
        
        for i in range(0, len(L)):
            sum = sum + (L[i])
        return (sum)


    def findSquareDigitSum(n):
        L=[]
        sum=0
        z=n
        while n>0:
            a=n%10
            n//=10
            L.append(a)
        
        for i in range(0, len(L)):
            sum = sum + (L[i])**2
        return (sum)





        


    







    if inp==1:
        getReverse(n)
        ans=="Y"
    if inp==2:
        checkPalindrome(n)
        ans="Y"
    if inp==3:
        checkNarcissistic(n)
        ans="Y"
    if inp==4:
        findDigitSum(n)
        if n<10:
            print(n)
        else:
            finalsum=0
            while n>10:
                n=findDigitSum(n)
                finalsum+=n
            print(finalsum)
        ans="Y"
    if inp==5:
        findSquareDigitSum(n)
        if n<10:
            print(n**2)
        else:
            finalsum=0
            while n>10:
                n=findSquareDigitSum(n)
                finalsum+=n
            print(finalsum)
        ans="Y"
    elif inp==6:
        exit()