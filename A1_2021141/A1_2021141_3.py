d=int(input("Enter degree"))

if d==3:
    coeff1=float(input("Enter coeff of x^3"))
    coeff2=float(input("Enter coeff of x^2"))
    coeff3=float(input("Enter coeff of x"))
    coeff4=float(input("Enter coeff of x^0"))
    lb=int(input("lower bound"))
    ub=int(input("upper bound"))
    inc=int(input("increment steps"))
    for k in range (lb,ub+1,inc):
        z=coeff1*(k**3)+coeff2*(k**2)+coeff3*k+coeff4
        if z<int(z)+0.5:
            z=int(z)
        else:
            z=int(z+1)
        if z<0:
            print(0)
        else:
            print('*'*z)
  
elif d==2:
    coeff1=float(input("Enter coeff of x^2"))
    coeff2=float(input("Enter coeff of x"))
    coeff3=float(input("Enter coeff of x^0"))
    lb=int(input("lower bound"))
    ub=int(input("upper bound"))
    inc=int(input("increment steps"))
    for k in range (lb,ub+1,inc):
        z=round(coeff1*(k**2)+coeff2*(k)+coeff3)
        if z<int(z)+0.5:
            z=int(z)
        else:
            z=int(z+1)
        if z<0:
            print(0)
        else:
            print('*'*z)
        
elif d==1:
    coeff1=float(input("Enter coeff of x"))
    coeff2=float(input("Enter coeff of x^0"))
    lb=int(input("lower bound"))
    ub=int(input("upper bound"))
    inc=int(input("increment steps"))
    for k in range(lb,ub+1,inc):
        z=round(coeff1*k+coeff2)
        if z<int(z)+0.5:
            z=int(z)
        else:
            z=int(z+1)
        if z<0:
            print(0)
        else:
            print('*'*z)
        


elif d==0:
    coeff1=float(input("Enter coeff of x^0"))
    lb=int(input("lower bound"))
    ub=int(input("upper bound"))
    inc=int(input("increment steps"))
    for k in range(lb,ub+1,inc):
        z=round(coeff1)
        if z<int(z)+0.5:
            z=int(z)
        else:
            z=int(z+1)
        if z<0:
            print(0)
        else:
            print('*'*z)
       



    


