#number of positive and negative numbers
p=0
n=0
for i in range(1,11):
    a=int(input("Enter the number: "))
    if(a<0):
        p+=1
    elif(a>0):
        n+=1
print("Total number of positive integers: ",p)
print("Total number og negative Integers: ",n)
