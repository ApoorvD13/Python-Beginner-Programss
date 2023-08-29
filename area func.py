def area(x,y):
    a=x*y
    return(a)
def vol(z):
    a=area(x,y)
    v=a*z
    return(v)
l=int(input("Enter length of the cuboid: "))
b=int(input("Enter breadth of the cuboid: "))
h=int(input("Enter height of the cuboid: "))
a=area(l,b)
v=vol(h)
print("The volume of the cuboid is: {} and the area is: {}".format(v,a))