def converting(a,b,number):
   
    
    finalnumber=0
    number=number[::-1]
    #converting to decimal
    for i in range(len(number)):
        if number[i] in ('0','1','2','3','4','5','6','7','8','9','.','-'): 
            if int(number[i])<(a-1):
                finalnumber+=int(number[i])*((a)**i)
            if int(number[i])>(a-1):
                print("wrong")
                exit()
            
        else:
                    
            anum= ord(number[i].upper()) - 55
            if anum<a:
                finalnumber+=(anum)*((a)**i)
            else:
                print("wrong")
                exit()



    #converting to radix needed
    l=[]
    quo=finalnumber
    while quo>0:
        hello=quo%b
        if hello > 9 :
            hello = chr(hello+55)
            l.append(hello)
        else:
            l.append(hello)
        quo=quo//b
    l=l[::-1]
    for i in l:
        print(i, end='')




























print('1) Convert decimal to binary and vice-versa \n 2) Convert decimal to hexadecimal and vice-versa \n 3) Convert decimal to octal and vice-versa.\n4) Convert binary to hexadecimal and vice-versa.\n 5) Convert binary to octal and vice-versa.\n 6) Convert hexadecimal to octal and vice-versa.\n 7) Convert number with radix A to radix B.')

n=input("Enter your choice number")
if n=='1':
    print('1. Decimal to binary\n  2.Binary to decimal')
    subchoice=input("Enter your subchoice number")
    number=str(input("Enter number in the given radix"))
    if subchoice=='1':
        converting(10,2,number)
    if subchoice=='2':
        converting(2,10,number)
if n=='2':
    print('1. Decimal to hexadecimal\n  2.hexadecimal to decimal')
    subchoice=input("Enter your subchoice number")
    number=str(input("Enter number in the given radix"))
    if subchoice=='1':
        converting(10,16,number)
    if subchoice=='2':
        converting(16,10,number)
if n=='3':
    print('1. Decimal to octal\n  2.octal to decimal')
    subchoice=input("Enter your subchoice number")
    number=str(input("Enter number in the given radix"))
    if subchoice=='1':
        converting(10,8,number)
    if subchoice=='2':
        converting(8,10,number)
if n=='4':
    print('1. binary to hexadecimal\n  2.hexadecimal to binary')
    subchoice=input("Enter your subchoice number")
    number=str(input("Enter number in the given radix"))
    if subchoice=='1':
        converting(2,16,number)
    if subchoice=='2':
        converting(16,2,number)
if n=='5':
    print('1. binary to octal\n  2.octal to binary')
    subchoice=input("Enter your subchoice number")
    number=str(input("Enter number in the given radix"))
    if subchoice=='1':
        converting(2,8,number)
    if subchoice=='2':
        converting(8,2,number)
if n=='6':
    print('1. hexadecimal to octal \n  2.octal to hexadecimal')
    subchoice=input("Enter your subchoice number")
    number=str(input("Enter number in the given radix"))
    if subchoice=='1':
        converting(16,8,number)
    if subchoice=='2':
        converting(8,16,number)
if n=='7':

    a=int(input("Enter radix A"))
    b=int(input("Enter radix B"))
    number=str(input("Enter number in the given radix"))
    
    converting(a,b,number)
    
       


    




