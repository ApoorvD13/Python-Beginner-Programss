'''l=[1,1,2,2,3,4,5,6,6,7,7]
u=[]
for i in l:
    if(i not in u):
        u.append(i)
print(u)'''
l=[1,2,3,4,5,6,7]
u=[5,6,7,8,9]
c=[]
for i in l:
    if(i in u):
        c.append(i)
print(c)