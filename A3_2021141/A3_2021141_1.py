import math


  







def matmul(matrixA,matrixB):
  
  

    
    blankmatrix= []
    for i in range(len(matrixA)):
        blankrow = []
        for j in range(len(matrixB[0])):
            blankrow.append(0)
        blankmatrix.append(blankrow)
    






    for i in range (len(matrixA)):
        for j in range(len(matrixB[0])):
            cuz=0
            for k in range(len(matrixB)):
                cuz+=float(matrixA[i][k])*float(matrixB[k][j])
            blankmatrix[i][j]=cuz
            
    
    
    return (blankmatrix)









'''matrixA=[]
rows=int(input("enter rows"))

for i in range(rows):
        ele=[i for i in input().split()]
        matrixA.append(ele)
print(matrixA)
columns=len(ele)
matrixB=[]
rowsb=int(input("enter rows"))

for i in range(rowsb):
        ele=[i for i in input().split()]
        matrixB.append(ele)
print(matrixB)
columnsb=len(ele) '''











def scale(x,y,z,sx,sy,sz):
    T=[[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]
    varim=[[x],[y],[z],[1]]
    scaled=matmul(T,varim)
    xnew=scaled[0][0]
    ynew=scaled[1][0]
    znew=scaled[2][0]
    return xnew,ynew,znew


def translate(x,y,z,tx,ty,tz):
    T=[[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]]
    varim=[[x],[y],[z],[1]]
    scaled=matmul(T,varim)
    xnew=scaled[0][0]
    ynew=scaled[1][0]
    znew=scaled[2][0]
    return xnew,ynew,znew

def rotate(x,y,z,axis,phi):
    if axis=='z':
        T=[[math.cos(phi),-math.sin(phi),0,0],[math.sin(phi),math.cos(phi),0,0],[0,0,1,0],[0,0,0,1]]
        
        varim=[[x],[y],[z],[1]]
        print(varim)
        scaled=matmul(T,varim)
        print(scaled)
        xnew=(round(scaled[0][0],1))
        ynew=(round(scaled[1][0],1))
        znew=(round(scaled[2][0],1))
        return xnew,ynew,znew
    if axis=='x':
        T=[[1,0,0,0],[0,math.cos(phi),-math.sin(phi),0],[0,math.sin(phi),math.cos(phi),0],[0,0,0,1]]
        
        varim=[[x],[y],[z],[1]]
        
        scaled=matmul(T,varim)
        
        xnew=(round(scaled[0][0],1))
        ynew=(round(scaled[1][0],1))
        znew=(round(scaled[2][0],1))
        
        return xnew,ynew,znew

    if axis=='y':
        T=[[math.cos(phi),0,math.sin(phi),0],[0,1,0,0],[-math.sin(phi),0,math.cos(phi),0],[0,0,0,1]]
        varim=[[x],[y],[z],[1]]
        scaled=matmul(T,varim)
        xnew=(round(scaled[0][0],1))
        ynew=(round(scaled[1][0],1))
        znew=(round(scaled[2][0],1))
        return xnew,ynew,znew

    

        



