from bank1 import accounts
from bank2 import main
class cal(accounts):
    def withdraw(self):
        w=int(input('Enter the amount you want to withdraw: '))
        cl=main()
        self.bal[1]=self.bal[1]-w
        self.acc=self.bal
        print('New Balance: ', self.bal[1])
    def depo(self):
        a = int(input('Enter the amount you want to withdraw: '))
        cl = main()
        self.bal[1] = self.bal[1] + a
        self.acc = self.bal
        print('New Balance: ', self.bal[1])
    def disp(self):
        print('Balance: ',self.bal[1])