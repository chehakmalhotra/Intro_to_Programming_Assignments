N=int(input("enter dimension of matrix"))
matrix=[]
for i in range (N):
    L=["enter space separated values for row"]
    L=[i for i in input().split()]
    matrix.append(L)
matrixcopy=[i[::-1] for i in matrix]
print("1) Normal traversal")
print('2) Alternating traversal')
print('3) Spiral traversal from outer to inwards')
print('4) Boundary traversal.')
print('5) Diagonal traversal from right to left')
print('6) Diagonal traversal from left to right.')
option=input("Enter option number")


def removalfunction(matrix,N):
    
    for i in range(1,N-1):
        
        matrix[i].pop(0)
        matrix[i].pop(-1)
    matrix.pop(0)
    matrix.pop(-1)
    return matrix
    
    

def boundary(matrix,N):
    if len(matrix)==1:
        print(matrix[0][0])
    else:
        for k in matrix[0]:
            print(k, end=' ')
    

        for i in range(1,N):
            print(matrix[i][N-1], end=' ')
        
        print(*matrix[N-1][N-2::-1], end=' ')

        for j in range(N-2,0,-1):
            print(matrix[j][0], end=' ')
    



if option=='3':
    for j in range(N,0,-2):
        boundary(matrix,j)
        matrix=removalfunction(matrix,j)
    

    









if option=='1':
    for i in matrix:
        for k in i:
            print(k,end=' ')
if option=='2':
    for i in range(N):
        if i%2==0:
            for k in matrix[i]:
                print(k, end=' ')
            
        else:
            reversedrow=matrix[i][::-1]
            for k in reversedrow:
                print(k, end=' ')












if option=='4':
    boundary(matrix,N)
    
    
if option=='5':






    
    for i in range(2*N-1):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if j+k==i:
                    print(matrix[j][k],end=" ")
    print()
       
           
if option=="6":

    for i in range(2*N-1):
        for j in range(len(matrixcopy)):
            for k in range(len(matrixcopy)):
                if j+k==i:
                    print(matrixcopy[j][k],end=" ")
    print()