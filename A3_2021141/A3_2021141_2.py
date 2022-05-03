class LaundryService:
    def __init__(self, customername, customercontact, email, typeofcloth, branded, season):
        global id
        self.id=id
        id+=1
        self.name=customername
        self.contact=customercontact
        self.email=email
        self.cloth=typeofcloth
        self.branded=branded
        self.season=season
        
    def customerDetails(self):
        print("Custoner ID is",self.id)
        print("Customer name is",self.name)
        print("Contact",self.contact)
        print("Email",self.email)
        print("Type of cloth",self.cloth)
        print("Branded or not",self.branded)
        
    def calculateCharge(self):
        charge=0
        if self.cloth=="Cotton":
            charge+=50
        elif self.cloth=="Silk":
            charge+=30
        elif self.cloth=="Woolen":
            charge+=90
        elif self.charge=="Polyester":
            charge+=20
        
        if self.branded==True:
            charge*=1.5
           
        
        if self.season=="Winter":
            charge/=2
            
        else:
            charge*=2
        return charge
    def finalDetails(self):
        self.customerDetails()
        x=self.calculateCharge()
        print("Total charge is",x)
        if x>200:
            print ('To be returned in 4 days')
        else:
            print('To be returned in 7 days')
id=1
for i in range(4):
    customername=input('Enter customer name')
    customercontact=int(input("Enter contact number"))
    email=input("Enter email")
    typeofcloth=input("Enter type")
    branded=bool(int(input("Is it branded")))
    season=input("enter season")
    c=LaundryService(customername, customercontact, email, typeofcloth, branded, season)
    c.finalDetails()









        

