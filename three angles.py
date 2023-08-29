a1=int(input("Enter the first angle: "))
a2=int(input("Enter the second angle: "))
a3=int(input("Enter the third angle: "))
if(a1+a2+a3==180):
    print("the triangle is possible!")
    if(a1==90 or a2==90 or a3==90):
        print("it is a right angle triangle ")
    elif(a1==a2==a3):
        print("it is an equilateral triangle ")
    elif(a1==a2 or a2==a3 or a1==a3):
        print("it is an isoceles triangle ")
else:
    print("the triangle is not possible ")