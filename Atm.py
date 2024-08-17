class BankATM:
    bal=5000
    def login(self,pin):
        if pin==2343:
            return True
        else:
            return False
    def credit(self,amt):
        self.bal+=amt
    def debit(self,amt):
        self.bal-=amt
    def show(self):
        print("current balance is=",str(self.bal))
obj=BankATM()
flag=False
for i in range(1,4):
    if obj.login(int(input("enter the pin code"))):
        flag=True
        break
if flag:
    while True:
        ch=input(""" c for credit
                 d for debit
                 b for balance
                e for exit /n""")
        print("/n")
        if ch=='c' or ch=='C':
            obj.credit(int(input("enter the amount")))
            print("after credit valueable balance is")
            obj.show()
        elif ch=='d' or ch=="D":
            amt=int(input("enter the amt for debit"))
            if amt<obj.bal:
                obj.debit(amt)
                print("after debit available balance is")
                obj.show()
            else:
                print("insuffisiant balance")
        elif ch=='b' or ch=='B':
            print(obj.bal)
        elif ch=='e' or ch=='E':
            break;
else:
    print("invlaid Pin Code")