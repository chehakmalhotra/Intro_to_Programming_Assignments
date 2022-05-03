n=int(input("Enter number of students"))
i=0
while i<n:
    s=input('Choose 2D or 3D')
    if s=='2D':
        print ("Choose 1.Square\n",'2.Rectangle\n','3.Rhombus\n','4.Parallelogram\n','5.Circle\n')
        choice=input("Enter number")
        if choice=='1':
            s=float(input("Enter the side s of the square"))
            print('The Perimeter of the square is',s*4)
            print('The Area of the square is', s**2)
        elif choice=='2':
            l=float(input("Enter the length l of the rectangle"))
            b=float(input("Enter the breadth b of the square"))
            print('The Perimeter of the rectangle is',2*(l+b))
            print('The Area of the rectangle is',l*b)
        elif choice=='3':
            a=float(input("Enter the side a of the rhombus"))
            d1=float(input("Enter the diagonal d1 of the rhombus"))
            d2=float(input("Enter the diagonal d2 of the rhombus"))
            print('The Perimeter of the rhombus is', a*4)
            print('The Area of the rhombus is',d1*d2)
        elif choice=='4':
            l=float(input("Enter the length l of the parallelogram"))
            b=float(input("Enter the breadth b of the parallelogram"))
            h=float(input("Enter the height h of the parallelogram"))
            print('The Perimeter of the parallelogram is', 2*(l+b))
            print('The Area of the is parallelogram',b*h)
        elif choice=='5':
            r=float(input("Enter the radius r of the circle"))
            print('The Perimeter of the circle is', (22/7)*r)
            print('The Area of the circle is',(22/7)*r*r)
        i+=1   







            

    elif s=='3D':
        print ('Choose 1.Cube \n2.Cuboid \n3.Right circular cone \n4.Hemisphere \n5.Sphere  \n6.Solid cylinder  \n7.Hollow cylinder')
        choice=input("Enter number")
        if choice=='1':
            s=float(input("Enter the side s of the cube"))
            print('The CSA of the cube is',s*s*4)
            print('The TSA of the cube is', s*s*6)
            print('The volume of the cube is', s*s*s)
        elif choice=='2':
            l=float(input("Enter the length l of the cuboid"))
            b=float(input("Enter the breadth b of the cuboid"))
            h=float(input("Enter the height h of the cuboid"))
            print('The CSA of the cuboid is',2*(l+b)*h)
            print('The TSA of the cuboid is',2*(l*b+b*h+l*h))
            print ('The volume of the cuboid is', l*b*h)
        elif choice=='3':
            r=float(input("Enter the radius of the cone"))
            h=float(input("Enter the height of the cone"))
            l=float(input("Enter the slant height of the cone"))
            print('The CSA of the cone is', (22/7)*r*l)
            print('The TSA of the cone is',(22/7)*r*(r+l))
            print('The volume of the cone is',(1/3)*(22/7)*r*r*h)
        elif choice=='4':
            r=float(input("Enter the radius r of the hemisphere"))
            print('The CSA of the hemisphere is', 2*(22/7)*r*r)
            print('The TSA of the hemisphere is',3*(22/7)*r*r)
            print('The volume of the hemisphere is',(2/3)*(22/7)*r*r*r)
        elif choice=='5':
            r=float(input("Enter the radius r of the sphere"))
            print('The CSA of the sphere is', 4*(22/7)*r*r)
            print('The TSA of the sphere is',4*(22/7)*r*r)
            print('The volume of the sphere is',(4/3)*(22/7)*r*r*r)
        elif choice=='6':
            r=float(input("Enter the radius of the cylinder"))
            h=float(input("Enter the height of the cylinder"))
            print('The CSA of the cylinder is', (22/7)*r*h*2)
            print('The TSA of the cylinder is',(22/7)*r*(r+h)*2)
            print('The volume of the cylinder is',(22/7)*r*r*h)
        elif choice=="7":
            r1=float(input("Enter the inner radius of the cylinder"))
            r2=float(input("Enter the outer radius of the cylinder"))
            h=float(input("Enter the height of the cylinder"))
            print('The CSA of the cone is', 2*(22/7)*h*(r1+r2))
            print('The TSA of the cone is',2*(22/7)*h*(r1+r2)+2*(22/7)*(r2-r1))
            print('The volume of the cone is',(22/7)*(r2-r1)*h)
        i+=1
        





               
                
                

