'''def pal(n):
    c = n
    r=0
    while(n>0):#1234
        d=n%10#4,3
        n//=10#123,12
        e=r*10#0,40
        r=e+d#4,43
    print(r)
    if(r==c):
        print("The number is a palindrome ")
    else:
        print("The number is not a palindrome")
a=int(input("Enter the number: "))
pal(a)'''
def lis():
    flag=0
    r = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 0]
    n = int(input("Enter the number to search "))
    for i in r:
        if(i==n):
            flag=1
    if(flag==1):
        print("The number you entered is present")
    else:
        print("The number is not present in the list")
p=int(input("How many numbers to search: "))
while(p>0):
    lis()
    p-=1




