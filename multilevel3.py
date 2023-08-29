from multileveli2 import sal

class gross(sal):
    def gross_sal(self):
        if(self.s<=50000):
            self.g=self.s-(self.s*0.1)
        elif (self.s <= 80000):
            self.g = self.s - (self.s * 0.25)
        elif (self.s <= 100000):
            self.g = self.s - (self.s * 0.35)
    def display(self):
        print('Name: ',self.n)
        print('ID: ', self.id)
        print('Department: ', self.dept)
        print('Base Salary: ',self.s)
        print('Gross Salary: ', self.g)
employ=[]
for i in range(3):
    emp1=gross()
    emp1.data()
    employ.append(emp1)
for i in range(3):
    employ[i].cal()
    employ[i].gross_sal()
    employ[i].display()
