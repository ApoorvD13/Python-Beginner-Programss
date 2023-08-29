from inheritance import area
class volume(area):
    def __init__(self):
        self.h = int(input("Enter length: "))
        self.j = int(input("Enter breadth: "))
        self.z=int(input('Enter height: '))
    def cal(self,a):
        self.a=a
        vol=a*self.z
        print('Volume is: ',vol)

obj1=volume()
x=obj1._rectangle(obj1.h,obj1.j)
obj1.cal(x)
