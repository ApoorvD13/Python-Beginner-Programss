class area:
    def areacir(self):
        self.r = int(input("Enter the radius: "))
        a=self.r*3.14*self.r
        print("Area of the circle is: ",a)
    def arearect(self):
        self.l=int(input("Enter the length: "))
        self.b = int(input("Enter the breadth: "))
        print('Area of the rectangle is: ',self.l*self.b)
    def areasq(self):
        self.s=int(input("Enter the length of side: "))
        print("The area of the square is: ",4*self.s)

