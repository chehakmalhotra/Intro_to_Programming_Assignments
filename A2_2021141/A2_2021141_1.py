while True:   
    print('Enter your choice: \n 1. Display specific Word Count \n  2. Display all Unique Words \n 3.Display all Word Counts \n 4.Replace word \n 5.Quit')
    n=int(input('enter option'))
    if n==1:
        w=input("enter word required")
        with open("question1_input.txt","r") as f:
            L= f.readlines()
            c=0
            for i in L:
                for k in i.split():
                    if k==w:
                        c+=1
                    
        print('Word count',c)
    if n==2:
        with open("question1_input.txt","r") as f:
            uniquewords =[]
            L=f.readlines()
            for i in L:
                for k in i.split():
                    if k not in uniquewords:
                        uniquewords.append(k)
        for i in uniquewords:
            print(i, end = "; ")
    if n==3:
        d={}
        with open("question1_input.txt","r") as f:
            allwords =[]
            uniquewords =[]
            L=f.readlines()
            for i in L:
                for k in i.split():
                    allwords.append(k)
                    if k not in uniquewords:
                        uniquewords.append(k)
            for j in uniquewords:
                d[j]=allwords.count(j)

        print('Word counts:')
        for o in d: 
            print(o,':',d[o])
    if n==4:
        old=input('enter old word')
        new=input('enter new word')
        with open("question1_input.txt","r") as f:
            L=f.readlines()
            l=''
            for i in L:
                for k in i.split():
                    if k==old:
                        l+=new+' '
                    else:
                        l+=k+' '
        with open("question1_input.txt","w") as f:
            f.write(l)
    if n==5:
        break



       










                
   


            

    





