
#create
dictionary1 = {1:"a", 2:"b", 3:"c"}
#access
print(dictionary1[1])

#updating
dictionary1[1]="hello"

print(dictionary1)

#delete
del dictionary1[1]

dictionary1.clear() # to clear it but keep the variable

print(dictionary1.keys())
print(dictionary1.values())
