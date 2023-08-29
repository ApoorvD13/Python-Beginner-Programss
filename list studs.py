roll=[21,22,23,24,25]
marks=[78,89,90,98,78]
a=int(input("Enter the roll number of the student: "))
if a not in roll:
    print("The student was absent for the test")
else:
    p=roll.index(a)
    print("Marks of roll number {} are {} ".format(a,marks[p]))
    gate=input("Do you want to modify marks: ")
    if(gate=='yes'):
        m=int(input("Enter the modified marks: "))
        marks[p]=m
    print("New marks of roll no {} are {} ".format(a,marks[p]))
#HOMEWORK: add and remove student using nested list, if already there ask to modify
#HOMEWORK: atm program to display balance add and withdraw money(check pin and ac number)
