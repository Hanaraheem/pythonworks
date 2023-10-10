                #program2
class Bank:
    bankname:str
    personname:str
    ifcd:str          #attributes
    branch:str  #instance variable
    accno:int
    amount:int
    balance:int

    def create(self,bankname,personname,ifcd,branch,accno,amount,balance): #method1
        self.bankname=bankname #self.attri=
        self.personname=personname
        self.ifcd=ifcd
        self.branch=branch
        self.accno=accno
        self.amount=amount
        self.balance=balance

    
    def deposit(self,amount):#method2
        self.balance+=amount
        print(f"your {self.bankname}has been credicted with amount{amount}avl bal {self.balance}")

    def withdraw(self,amount):#method3
        if amount>self.balance:
            print("insufficient balance transaction declined")
        else:
            self.balance-=amount
            print(f"your {self.bankname} has been debited with amount{amount} avl bal {self.balance}")
        
    def get_balance(self):#method4
        print(f"your avl bal{self.balance}")

obj=Bank() #objt create
obj.create("sbi","hana","ssfddddd11","aluva",34005565770,4500,6000)


obj.deposit(5000) #deposit

obj.withdraw(3000)


