n=int(input("Start: "))
n1=int(input("Stop: "))
'''for j in range(n,n1):
    for i in range(2, j):
        if (j % i == 0):
            break
        print(j)
        break'''
i=n
j=2
while(i<n1):
    while(j<i):
        if(i%j==0):
            break
        print(i)
        break
        j+=1
    i += 1



