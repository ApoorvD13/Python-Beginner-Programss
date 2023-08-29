class per():
    def __init__(self):
        self.m=int(input("Enter Lower Limit: "))
        self.n=int(input("Enter Upper Limit: "))
    def square(self):
        for i in range(self.m,self.n+1):
            j=i ** 0.5 *10
            if(j%10==0):
                print(i)
ps=per()
ps.square()