# 26.05.2019

# no type needed
var1 = 500
var2 = 56.432
var3 = "hallo"

# multiple assignment
a = b = c = 7


print("Int",var1)
print("float",var2)
print("string",var3)
print(a,b,c)

# various string print things
print(var3[0]) # print the specific char from the string
print(var3[0:3]) # print from 0 to 3 char
print(var3[1:]) # print everything starting from char 1 to the end

print(var3[:]) # print everything
print(var3[:2])# print from beginning to char 2

var1 = 0
var2 = 3
print(var3[var1:var2]) # print through vars

# del deletes a variable

del var1

print(var1)