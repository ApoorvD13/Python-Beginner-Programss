class div():
    def __init__(self):
        self.n=int(input('Enter upper limit (starting from one): '))
    def divs(self):
        count = 0
        print("Numbers ending with 5 ")
        for i in range(1,self.n+1):
            if(i%5==0):
                if(i%10==5):
                    print(i)
                elif(i%10==0):
                    count+=1
        print('The number of digits ending with zero are: ',count)

d1=div()
d1.divs()

