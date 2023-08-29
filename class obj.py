class calc:
    def add(self):
        self.a=int(input("Enter first number: "))
        self.b=int(input('Enter second number: '))
    def ans(self):
        c=self.a-self.b
        return(c)

cv=calc()
cv1=calc()
cv1.add()
print(cv1.ans())
cv.add()
print(cv.ans())