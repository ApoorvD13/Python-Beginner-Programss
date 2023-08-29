i=1
s=0
while(i<11):
    a=int(input("Enter the number: "))
    if(a>0):
        s+=a
    else:
        break
    i+=1
print("Sum of positive integers is: ",s)
