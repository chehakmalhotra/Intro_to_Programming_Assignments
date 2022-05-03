p, q=[int(x) for x in input("Enter two values: ").split()]
m, n=[int(x) for x in input("Enter two values: ").split()]
matrix=[]
for i in range(m):
    l=[int(i) for i in input()]
    matrix.append(l)

d={}
for i in range(n):
    for j in matrix:
        if i in d.keys():
            d[i]+=j[i]
            
        else:
            if j[i]==1:
                d[i]=1
            elif j[i]==0:
                d[i]=0



dd=[]
ds=[]

finald=dict(sorted(d.items(), key=lambda item: item[1], reverse=True))


anewlist=list(finald.items())


for a in range(n):
    if a%2==0:
        dd.append(anewlist[a][1])
    else:
        ds.append(anewlist[a][1])



fandd=0
na=p
for b in dd:
    
    fandd+=b*na
    na+=2


fands=0
nap=q+1
for c in ds:
    fands+=c*nap
    nap+=2

print(fandd, fands)



dd2=[]
ds2=[]
for f in range(n):
    if f%2==0:
        dd2.append(anewlist[f][0])
    else:
        ds2.append(anewlist[f][0])



for e in dd2:

    for moreele in matrix:
        if moreele[e]==1:
            moreele[e]='D'


for g in ds2:
    for ele4 in matrix:
        if ele4[g]==1:
            ele4[g]='S'
for i in matrix:
    for z in i:
        print(z, end='')
    print()
    

