import cases 

def function2(list):
    if len(list)==1:
        return list[0]
    else:
        return list[0]+function2(list[1:]) 



def testing():
    newn=cases.generateData()
    s=0
    for i in range(newn):
        with open('Inputfile{}'.format(i+1),'r') as f:
            input2=f.readline()
        hil= input2.strip('][').split(', ')
        
        hil2=[float(i) for i in hil]

        output2=str((function2(hil2)))
        print(output2)
        
        with open('Outputfile{}'.format(i+1),'r') as j:
            output1=j.readline()

        print(output1)
        if output1==output2:
            s+=1
    if s==newn:
        print("success")
    else:
        print("failed")

testing()

    