n=int(input("Enter the number of elements: "))
flag=0
lis=[]
for p in range(n):
    e=int(input("Enter the Element: "))
    lis.append(e)
for j in range(1,len(lis)):
    p = 0
    b = 0
    for k in range(j):
        p+=lis[k]
        #print(p,'LEFT')
    for i in range(j+1,len(lis)):
        b+=lis[i]
        #print(b,"RIGHT")
    if (p == b):
        flag = 1
        break
if(flag==1):
    print(lis[j])
else:
    print(0)
