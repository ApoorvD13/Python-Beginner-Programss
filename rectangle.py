rl1 = int(input("Enter the length of the first rectangle: "))
rb1 = int(input("Enter the breadth of the first rectangle: "))
rl2 = int(input("Enter the length of the second rectangle: "))
rb2 = int(input("Enter the breadth of the second rectangle: "))
a1 = rl1*rb1
a2 = rl2*rb2
if(a1>a2):
    print("Rectangle one is larger ")
elif(a1==a2):
    print("Both the rectangles are of the same size ")
else:
    print("Rectangle two is larger ")