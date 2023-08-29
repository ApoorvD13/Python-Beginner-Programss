'''abc=open('sample.txt','r')
print(abc.read())
abc.close()'''
def write():
    file=open("empdata.txt",'w')
    n = int(input('How many employees you want to enter? '))
    for i in range(n):
        name=input('Enter the first name of the employee ')
        id=input('Enter employee ID ')
        file.write(name+' '+id+' \n')
    file.close()
def read():
    l2=[]
    emp=input("Enter name and ID of the employee you want to search ")
    str1='x'
    file=open('empdata.txt','r')
    while str1:
        str1=file.readline()
        l2=str1.split(' ')
        print(str1)
        print(l2)
        if(emp==l2[1]):
            print("Employee is present in the database! ")
            break
    file.close()
write()
read()


