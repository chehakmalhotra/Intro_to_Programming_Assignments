class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
    def object_info(self):
        print(self.firstname,self.lastname,self.age)
       
    
    def sort_attribute(self,name,fnl,lnl,al):
        if name=="firstname":
            fnl.sort()
           
            for i in fnl:##
              for j in chehak:##
                if j.firstname == i:##
                  print(f"{j.firstname} {j.lastname} {j.age}")##
            
    
        elif name=="lastname":
            lnl.sort()
           
            for i in lnl:##
              for j in chehak:##
                if j.lastname == i:##
                  print(f"{j.firstname} {j.lastname} {j.age}")##
        
        
        
        
        
        
        elif name=="age":
            al.sort()
          
            for i in al:##
              for j in chehak:##
                if j.age == i:##
                  print(f"{j.firstname} {j.lastname} {j.age}")##
                


chehak = [] ##
n=int(input("Enter no of ppl"))
k=int(input("Enter no of queries"))
fnl=[]
lnl=[]
al=[]
for i in range(n):
    l=[x for x in input().split()]
    firstname=l[0]
    lastname=l[1]
    age=l[2]
    fnl.append(firstname)
    lnl.append(lastname)
    al.append(age)
    chehak.append(Person(firstname,lastname,age))


for i in range(k):
    name=input("enter option")
    c=Person(firstname,lastname,age)
    c.sort_attribute(name,fnl,lnl,al)
    

        

