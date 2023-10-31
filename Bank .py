class bank:
    def __init__(self,name,num,bal):
        self.name=name
        self.num=num
        self.bal=bal
    def deposit(self):
        amt=int(input("Enter amount "))
        self.bal=amt
    def withdraw(self):
        amt=int(input("Enter amount "))
        self.bal-=amt
    def showbal(self):
        print(self.name,"\n",self.bal)
    
l=[]
def create():
    n=input("Enter name: ")
    m=int(input("Enter Accno: "))
    p=int(input("Enter Balance: "))
    x=bank(n,m,p)
    l.append(x)
while True:
    choice=int(input("Enter choice "))
    if choice==1:
        create()
    elif choice==2:
        accno=int(input("Enter accno: "))
        for i in l:
            if accno==i.num:
                i.deposit()
                i.showbal()
    elif choice==3:
        i.withdraw()
        i.showbal()
    else:
        print("Invalid!!")
        break
    