class student:
    def get(self,n,r,m):
        self.name=n
        self.roll=r
        self.marks=m
    def out(self):
        print("Name: ",self.name)
        print("Roll no: ",self.roll)
        print('Marks: ',self.marks)
st1=student()
st2=student()
st3=student()

st1.get('apoorv',24,20)
st2.get('Amogh',25,20)

st1.out()
st2.out()