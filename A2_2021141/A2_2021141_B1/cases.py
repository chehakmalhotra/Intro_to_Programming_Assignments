def function1(list):
    sum=0
    for i in list:
        sum+=i
    return sum

def generateData():
    n=int(input("enter number of inputs"))
    for i in range(n):
        L=[float(i) for i in input().split()]
        with open('Inputfile{}'.format(i+1),'w') as f:
            f.write(str(L))
        output=function1(L)
        with open('Outputfile{}'.format(i+1),'w') as j:
            j.write(str(output))
    return n
