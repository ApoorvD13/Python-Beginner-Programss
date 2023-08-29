class area:
    def __init__(self):
        self.x=int(input("Enter Length: "))
        self.y = int(input("Enter Breadth: "))
    def cal(self):
        self.a=self.x*self.y
        print("Area: ",self.a)

class volume(area):

    def __init__(self):
        self.h=int(input('Enter Height: '))
        super().__init__()
    def volume1(self):
        vol=self.a*self.h
        print('Volume: ',vol)
obj=volume()
obj.cal()
obj.volume1()
