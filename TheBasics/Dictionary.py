# 26.05.2019

dictionary = {}
dictionary[1] = 'Item 1'
dictionary[2] = 'Item 2'
dictionary["hello World"] = 'Item 3', 'Item 4', 8

print(dictionary)
print(dictionary[1])
print(dictionary["hello World"])
var1 = dictionary["hello World"]
print("test", dictionary["hello World"][2]+10) # looks like a tupel but is no tupel?
var2= dictionary["hello World"][2]
var2 +=2
print(var2)
print(var1[0:2]*4) 
print(var1[0]+' hallo') 

print(dictionary.values()) # print out all the values
print(dictionary.keys()) # print out all the keys

newDic = {var1:"hello", 2:"Item3", 3: 45} # key can be a variable
print(newDic)
print(newDic.keys())
print(newDic.values())