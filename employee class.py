emp=[]
class employee:
    def add(self):
        self.id = int(input("Enter the ID of the employee: "))
        self.name=input('Enter the Name of the employee: ')
        self.base=int(input('Enter the basic salary: '))
        self.net=self.base+self.base/100*15
    def dis(self):
        print('*********************************************')
        print('Name: ',self.name)
        print("Employee ID: ",self.id)
        print('Basic Salary: ',self.base)
        print('Net Salary: ',self.net)
        print('*********************************************')

ch=int(input(("Enter your choice\n1.Add Employee\n2.Remove an Employee\n3.Display Employee info\n4.EXIT ")))

while(ch!=4):
    if(ch==1):
        empob=employee()
        empob.add()
        emp.append(empob)
        print("Employee has been added Successfully! ")
        print('*********************************************')
    if(ch==2):
        id=int(input('Enter the ID of the employee: '))
        for i in emp:
            if(i.id==id):
                emp.remove(i)
        print("Employee Data has been successfully deleted! ")
        print('*********************************************')
    if(ch==3):
        for i in emp:
            i.dis()
    if(ch==4):
        break
    ch = int(input(("Enter your choice\n1.Add Employee\n2.Remove an Employee\n3.Display Employee info\n4.EXIT ")))




