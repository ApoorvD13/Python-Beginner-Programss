#addition of even numbers and odd numbers seperate
e=0
o=0
for i in range (1,11):
    a=int(input("Enter the number: "))
    if(a%2==0):
        e+=a
    else:
        o+=a
print("The addition of even numbers is ",e)
print("The addition of odd numbers is ",o)