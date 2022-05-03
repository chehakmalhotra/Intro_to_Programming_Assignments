from multiprocessing import AuthenticationError
from datetime import datetime
print(datetime.now())

class BankAccount:
    def __init__(self, username,password,iamount):
        self.username=username
        self.password=password
        self.iamount=iamount
        f=open ("username.txt",'a')


    def authenticate(self):
        spassword=input("enter secret password")
        if spassword==password:
            return True
        else:
            return False
    def deposit(self, depositamount):
        i=0
        try:
            while True:
                assert i<3
                if self.authenticate()==True:
                    break
                if self.authenticate()==False:
                    i+=1
        except:
            print("too many wrong attempts")
        self.iamount+=depositamount
        f=open("username.txt","a")

        f.write(f'{datetime.now()}The amount of Rupees{depositamount}has been added,Current balance,{self.iamount}')
            
        


    def withdraw(self,wamount):
        i=0
        try:
            while True:
                assert i<3
                if self.authenticate()==True:
                    break
                if self.authenticate()==False:
                    i+=1
        except:
            print("too many wrong attempts")
        if wamount>self.iamount:
            print('Low balance!!')
        else:
            self.iamount-=wamount
            f=open("username.txt","a")
            f.write(f'{datetime.now()}Timestamp The amount of Rupees{wamount}has been debited,Current balance,{self.iamount}')
            

    def bankStatement(self):
        i=0
        try:
            while True:
                assert i<3
                if self.authenticate()==True:
                    break
                if self.authenticate()==False:
                    i+=1
        except:
            print("too many wrong attempts")
        f=open("username.txt","r")
        z=f.readlines()
        for i in z:
            print(i)




        
            





username=input("Enter username")
password=input("Enter password")
iamount=int(input("Enter initial amount"))
c=BankAccount(username,password,iamount)
print('Select Your Option: 1.Deposit, 2.Withdraw, 3.Bank statemnt')
ans='Y'
while ans=='Y':
    op=input("enter op")
    if op=="1":
        depamo=int(input("enter deposit amount"))
        c.deposit(depamo)
    elif op=="2":
        wamo=int(input('enter withdraw amount'))
        c.withdraw(wamo)
    elif op=="3":

        c.bankStatement()
    ans=input("continue? Y/N")

