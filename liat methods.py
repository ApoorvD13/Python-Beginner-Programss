list1=[1,2,3,4,5,5,6,'apoorv']
list1.append(9)#insert element in a list at the last
list2=list1[2:6]#copy elemnets to another list(last position not included)
list1.remove(5)#remove first occurance of an element
list1.insert(3,'python')#insert element in any position
print("List 2: ",list2)
print(list1)
a=list1.pop(3)#remove last element and assign to a variable(if index not provided)
print(a)
print(list1.index(1))#to find index of an element