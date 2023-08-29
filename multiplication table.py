"""for i in range(1,11):
    for j in range(1,11):
        print(i*j,end="\t")
    print()"""
n=int(input("Start: "))
n1=int(input("Stop: "))
for i in range(n,n1+1):#10
    fact = 1
    for j in range(1,i+1):#1,10
       fact=fact*j
    print("Factorial of {} is {} ".format(i, fact))