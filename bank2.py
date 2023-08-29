from bank1 import accounts
from bank3 import cal

class main(accounts):
    def choice(self):
        self.ac=int(input('Enter your account number: '))
        if(self.ac in self.acc):
            self.bal=self.acc[self.ac]
            c=cal()
            print('Welcome ',self.bal[0])
            pin=int(input('Enter your PIN:'))
            if(pin==self.bal[2]):
                ch=int(input('Enter number to proceed:\n1.Deposit\n2.Withdraw\n3.Display Balance\n4.EXIT'))
                while(ch!=4):
                    if(ch==1):
                        c.depo()
                    elif(ch==2):
                        c.withdraw()
                    elif(ch==3):
                        c.disp()
                    ch = int(input('Enter number to proceed:\n1.Deposit\n2.Withdraw\n3.Display Balance\n4.EXIT'))
            else:
                print('Invalid PIN')
        else:
            print("Invalid Account Number!!")

