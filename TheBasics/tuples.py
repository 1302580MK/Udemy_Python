# 26.05.2019
# Tuples vs Lists

# Tuples are read only
# Tuples have ( ) brackets

# Example with a List:

awesomeList= ['hello', 45, 'Marc', 89.4]

awesomeList[3] = 6

# List can be updated

print(awesomeList)

# now a tuple

awesomeTuple = ('MarcTuple', 1, 213.2, 'Hello')

print(awesomeTuple)

print(awesomeTuple[2])

# ERROR awesomeTuple[2] = 3 
# Tuple object does not support item assignment

# ERROR awesomeTuple[1] +=3

# but slicing is working
print(awesomeTuple[0][2:5])
var7 = awesomeTuple[0][2:5]
var8 = awesomeTuple[2]
print(var7*3)
print(var8*3)

