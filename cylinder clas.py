class cylinder():
    def __init__(self,h,r):
        self.h=h
        self.r=r
    def vol(self):
        vol=3.14*self.r**2*self.h
        print("Volume of the cylinder is: ",vol)
    def sur(self):
        sur=2*3.14*self.r*self.h
        print("Surface area of the Cylinder is: ",sur)

c1=cylinder(3,6)
c2=cylinder(6,9)
c3=cylinder(10,12)
#cylinder 1
c1.vol()
c1.sur()
#cylinder 2
c2.vol()
c2.sur()
#cylinder 3
c3.vol()
c3.sur()
