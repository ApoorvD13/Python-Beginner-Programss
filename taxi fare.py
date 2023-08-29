d=int(input("enter the distance covered: "))
if(d<=5):
    f=100
    print("The toal fare of your taxi is ",f)
elif(5<d<=15):
    f=100+(d-5)*10
    print("The toal fare of your taxi is ",f)
elif(15<d<=25):
    f=200+(d-15)*8
    print("The toal fare of your taxi is ",f)
else:
    f=280+(d-25)*5
    print("The toal fare of your taxi is ",f)
