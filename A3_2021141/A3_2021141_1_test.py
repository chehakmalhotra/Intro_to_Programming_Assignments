import A3_2021141_1 as p

def test_matmul(A,B, true_C):
    z=p.matmul(A,B)
   
    assert z==true_C
    return True

def test_scale(x, y, z, sx, sy, sz, true_x, true_y, true_z):
    xnew,ynew,znew=p.scale(x, y, z, sx, sy, sz)
    assert xnew==true_x and ynew==true_y and znew==true_z
    return True
    

def test_translate(x, y, z, tx, ty, tz, true_x, true_y, true_z):
    xnew,ynew,znew=p.translate(x, y, z, tx, ty, tz)
    assert xnew==true_x and ynew==true_y and znew==true_z
    return True
   

def test_rotate(x, y, z, axis, phi, true_x, true_y, true_z):
    xnew,ynew,znew=p.rotate(x,y,z,axis,phi)
    assert xnew==true_x and ynew==true_y and znew==true_z
    return True
    





print("Choose what you want to check 1.matrix multiplication 2.scaling 3.transformation 4.rotation")
option=input("enter choice")
if option=='1':

    matrixA=[]
    rowsa=int(input("enter rows"))

    for i in range(rowsa):
            print("Enter space separated rows")
            elea=[i for i in input().split()]
            matrixA.append(elea)
    print(matrixA)
    columns=len(elea)
    matrixB=[]
    rowsb=int(input("enter rows"))

    for i in range(rowsb):
            print("Enter space separated rows")
            eleb=[i for i in input().split()]
            matrixB.append(eleb)
    print(matrixB)
    columnsb=len(eleb)

    yourans=[]
    rowsya=int(input("enter rows"))

    for i in range(rowsya):
            print("Enter space separated rows")
            eleya=[int(i) for i in input().split()]
            yourans.append(eleya)
    print(yourans)
    columns=len(eleya)


    test_matmul(matrixA,matrixB, yourans)

if option=='2':
    x=float(input("Enter value of x"))
    y=float(input("Enter value of y"))
    z=float(input("Enter value of z"))
    sx=float(input("enter scale for x"))
    sy=float(input("enter scale for y"))
    sz=float(input("enter scale for z"))
    true_x=float(input("Enter scaled x "))
    true_y=float(input("Enter scaled y "))
    true_z=float(input("Enter scaled z "))

    test_scale(x, y, z, sx, sy, sz, true_x, true_y, true_z)

if option=='3':
    x=float(input("Enter value of x"))
    y=float(input("Enter value of y"))
    z=float(input("Enter value of z"))
    tx=float(input("enter translation x"))
    ty=float(input("enter translation y"))
    tz=float(input("enter translation z"))
    
    true_x=float(input("Enter transformed x "))
    true_y=float(input("Enter transformed y "))
    true_z=float(input("Enter transformed z "))

    test_translate(x, y, z, tx, ty, tz, true_x, true_y, true_z)

if option=='4':
    x=float(input("Enter value of x"))
    y=float(input("Enter value of y"))
    z=float(input("Enter value of z"))
    phi=int(input("enter angle "))
    axis=input("enter axis")
    true_x=float(input("Enter rotated x "))
    true_y=float(input("Enter rotated y "))
    true_z=float(input("Enter rotated z "))

    test_rotate(x, y, z, axis, phi, true_x, true_y, true_z)











