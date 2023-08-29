from multiplei1 import employee
import random as r
class sal(employee):

    def cal(self):
        if(self.dept=='it'):
            self.s=r.randint(80000,100000)
        elif(self.dept=='hr'):
            self.s=r.randint(50000,80000)
        elif(self.dept=='marketing'):
            self.s=r.randint(10000,50000)

