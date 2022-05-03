class Company:
    def __init__(self,cname,requiredcgpa, branches, positionopen):
        self.branches=branches[0:]
        self.name=cname
        self.requiredcgpa=requiredcgpa
        self.positionopen=int(positionopen)
        self.appliedStudents=[]
        self.applicationopen=True
        
    def hireStudents(self, placed):
        self.appliedStudents.sort(key = lambda x:x[1], reverse = True)
        minno=min(self.positionopen, len(self.appliedStudents))
        selectstu=[]
        for i in range(minno):            
            selectstu.append(self.appliedStudents[i][0])
        if len(selectstu) > 0 :
            print('The company {} has selected the following students :'.format(self.name))
            for i in selectstu:
                print(i) 
        print ('Number of position still open {}'.format(self.positionopen - len(selectstu)))
        self.selected = len(selectstu)
        placed.extend(selectstu)
        self.closeApplication()


    def closeApplication(self):
        print('Number of students selected : ', self.selected)






class Student:
    def __init__(self,name,cgpa,branch):
        self.name=name
        self.cgpa=cgpa
        self.branch=branch
        
        self.isplaced=False
        
    def isEligible(self,o, placed):
        
        if self.cgpa>=o.requiredcgpa and self.branch in o.branches and self.isplaced==False and self.name not in placed:
            print(f"Student {self.name} is eligible for the company {o.name}")
            return True
        else:
            print(f'Student {self.name} is not eligible for Company {o.name}')
            return False


    def apply(self,o):
        o.appliedStudents.append([self.name, self.cgpa])
    def getsPlaced(self):
        self.isplaced=True


allstudents=[]
nstudents=int(input("Enter number of students"))
for i in range(1,nstudents+1):
    print("Enter details of student",i)
    name=input('Enter name of student')
    
    cgpa=float(input('Enter cgpa of student'))
    assert cgpa <=10, "Invalid value"
    branch=input('Enter branch of student')
    x=Student(name,cgpa,branch)
    allstudents.append(x)

    
 


placed = []  
ncompany=int(input('Enter number of companies'))
for i in range(1,ncompany+1):
    print("Enter details of company",i)
    namecompany=input('Enter name of company')
    requiredcgpa=float(input('Enter required cgpa of company'))
    print("Enter space separated branches")
    branch=[i for i in input().split()]
    positions=int(input("enter number of positions open"))
    o=Company(namecompany, requiredcgpa, branch, positions)
    for z in (allstudents):
        if z.isEligible(o, placed)==True:
            z.apply(o)
    o.hireStudents(placed)  