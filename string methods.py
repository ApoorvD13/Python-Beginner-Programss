a="hello this is @ a string"
print(len(a))#pritn the lenght of a

#print each letter individually
for x in "banana":
    print(x)

#break list into two parts
print(a.split('@'))
#splits from the charachter provoded

print(a.upper())
print(a.lower())
#convert string into uppercase or lowercase

a.replace('l','t')
#replace first letter with the second one
print(a[::-1])#reverse a string
