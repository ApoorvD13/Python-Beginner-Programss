y=int(input("Enter the year: "))
if(y%4==0):
    print("it is a leap year ")
elif(y%100==0):
    print("it is a century year ")
elif(y%4==0 and y%100==0):
    print("it is both a leap and a century year ")
else:
    print("it is neither leap nor a century year ")
