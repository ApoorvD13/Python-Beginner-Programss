'''s=input("Enter a string: ")
count=0
for i in s:
    if(i=='a'or i=='i'or i=='e'or i=='o'or i=='u'):
        count+=1
print('vowels=',count)'''

s=input("Enter a string: ")
count=0
v=s.split(' ')
print(v)
count=len(v)
for i in v:
    if (i==''):
        count-=1
print('words =',count)