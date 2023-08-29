from calc_class import calc
c=calc()
ch=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.EXIT\nEnter your choice: "))
while(ch!=5):
    a = int(input('Enter the first number: '))
    b = int(input('Enter the Second number: '))
    if(ch==1):
        c.add(a,b)
    if (ch == 2):
        c.sub(a, b)
    if (ch == 3):
        c.mul(a, b)
    if (ch == 4):
        c.dic(a, b)
    ch=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.EXIT\nEnter your choice: "))
