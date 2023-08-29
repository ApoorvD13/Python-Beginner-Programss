class stu:
    def __init__(self):
        self.r=int(input("Enter roll number of student: "))
        self.s1=int(input('Enter the marks in Maths: '))
        self.s2 = int(input('Enter the marks in Physics: '))
        self.s3 = int(input('Enter the marks in Chemistry: '))
        print("***************************************************")

all=[]
tofail=0
s1f=0
s2f=0
s3f=0
n=int(input('How many student you want to add? '))
for j in range(n):
    s=stu()
    all.append(s)

for i in all:
    if(i.s1<50 or i.s2<50 or i.s3<50):
        tofail+=1
        if(i.s1<50):
            s1f+=1
        if (i.s2 < 50):
            s2f += 1
        if (i.s3 < 50):
            s3f += 1
    else:
        print("All students are PASSED!")

print("Total Number of students who failed(at least one): ",tofail)
print("Total Number of students who failed in Maths: ",s1f)
print("Total Number of students who failed in Physics ",s2f)
print("Total Number of students who failed in Chemistry: ",s3f)


