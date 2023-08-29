class line:
    def dist(self,x,y):
        self.x=x
        self.y=y
        self.d=((self.x[1]-self.x[0])**2+(self.y[1]-self.y[0])**2)**0.5
        print("Distance: ",self.d)
    def slope(self):
        self.s=(self.y[1]-self.y[0])/(self.x[1]-self.x[0])
        print("Slope: ",self.s)

x=(2.56,5.5)
y=(1.23,9.6)
lin=line()
lin.dist(x,y)
lin.slope()