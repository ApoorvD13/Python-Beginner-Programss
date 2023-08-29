'''marks=[['apoorv',90],['abc',89],['xys',80]]
for i in range(3):
    for j in range(2):
        print(marks[i][j])'''
que=[['Who is the PM of India? ','Jawaharlal Nehru','Narendra Modi','Rahul Gandhi','Narendra modi'],\
     ['Capital of India?','Delhi','Mumbai','Bangalore','Delhi'],['Capital of Maharashtra?','Mumbai','Pune','Nagpur','Mumbai']]
s=0
for i in range(3):
    for j in range(4):
        print(que[i][j])
    print("********************************")
    p=input("Enter your answer: ").capitalize()
    if(p==que[i][4]):
        print("Correct Answer!")
        print("********************************")
        s+=1
    else:
        print("Wrong answer!")
print("Your Score is: ",s)

