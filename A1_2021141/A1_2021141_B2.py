e1, e2, e3 =(input("Enter origin of light ray: ").split())
e1=float(e1)
e2=float(e2)
e3=float(e3)
d1, d2, d3 =(input("Enter direction of light ray: ").split())
d1=float(d1)
d2=float(d2)
d3=float(d3)
xo, yo, zo =(input("Enter center of sphere: ").split())
xo=float(xo)
yo=float(yo)
zo=float(zo)
R=float(input("Enter radius"))
for t in range(1000):
    x1=float(e1+t*d1)
    x2=float(e2+t*d2)
    x3=float(e3+t*d3)
    x4=float(e1+(t+1)*d1)
    x5=float(e2+(t+1)*d2)
    x6=float(e3+(t+1)*d3)
    if (x1-xo)**2+(x2-yo)**2+(x3-zo)**2-R**2<=0 and (x4-xo)**2+(x5-yo)**2+(x6-zo)**2-R**2>=0 or (x1-xo)**2+(x2-yo)**2+(x3-zo)**2-R**2>=0 and (x4-xo)**2+(x5-yo)**2+(x6-zo)**2-R**2<=0:
        print ( "The ray with origin at",e1,e2,e3,"and direction",d1,d2,d3,"intersects the sphere with radius",R,"and center",xo,yo,zo,"at point",x1,x2,x3,"where t is equal to",t,"and point",x4,x5,x6,"where t is equal to",t+1)



