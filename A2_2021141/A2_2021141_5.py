def noteCreate():
    major='W W H W W W H'
    minor='W H W W H W W'
    majorscale="C C# D D# E F F# G G# A A# B"
    majorlist=major.split()
    minorlist=minor.split()

    majorscalelist=majorscale.split()

    f=open('scalemajor.txt','w')
    for inpu in majorscalelist:
        l=[]
        vari=majorscalelist[majorscalelist.index(inpu):len(majorscalelist)]+majorscalelist[0:majorscalelist.index(inpu)]
        stri = inpu + "'"
        vari.append(stri)     
        l.append(inpu)
        index=0
        for i in majorlist:
            if i=='W':
                index+=2
                var=vari[index]
                l.append(var)

                
            if i=='H':
                index+=1
                l.append(vari[index])
        ls=' '.join(l)   
        f.write(ls)
        f.write('\n')
    f=open('scaleminor.txt','w')
    for inpu in majorscalelist:
        l=[]
        vari=majorscalelist[majorscalelist.index(inpu):len(majorscalelist)]+majorscalelist[0:majorscalelist.index(inpu)]
        stri = inpu + "'"
        vari.append(stri)    
        l.append(inpu)
        index=0
        for i in minorlist:
            if i=='W':
                index+=2
                var=vari[index]
                l.append(var)

                
            if i=='H':
                index+=1
                l.append(vari[index])
        ls=' '.join(l)    
        f.write(ls+'\n')
noteCreate()     
majorscale="C C# D D# E F F# G G# A A# B C'"
majorscalelist=majorscale.split()

def majorNotes(root):
    f=open('scalemajor.txt','r')
    inpu=majorscalelist.index(root)
    vble=f.readlines()
    print(vble[inpu])

def minorNotes(root):
    f=open('scaleminor.txt','r')
    inpu=majorscalelist.index(root)
    vble=f.readlines()
    print(vble[inpu])

inpu=input('Enter the root note:')
scaletype=input('Enter the type of scale (Major/Minor):')
print('The {} scale in the key of {} is:'.format(scaletype,inpu))
if scaletype.lower()==("major"):
    majorNotes(inpu)
if scaletype.lower()==("minor"):
    minorNotes(inpu)









