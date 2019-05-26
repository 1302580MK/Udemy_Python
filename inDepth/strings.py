# 26.05.2019

# working with strings and their variations
# https://developers.google.com/edu/python/strings
string1 = "Python is indeed very amazing"

print(string1)
print(string1[-1]) # last element
print(string1[0:5]) # element 0 - 4

# update strings

print(string1[:4] + " bob") # appending

string2 = "Python is the best"

print("Hello \n World") # escape character

string3 = string1 + ' ' + string2
print(string3)

var1 = "Hello"
var2 = "Marc"

print("%s this is the best %s" % (var1, var2))

lorem = """ Lorem ipsum dolor sit amet, consetetur sadipscing 

elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. """

#print(lorem) # """ allows to format text and have a lot of it

var4="marc"
print(var4.capitalize()) # capitalize the first letter
print(var4.upper()) # uppercases every letter
print("find more here: https://developers.google.com/edu/python/strings ")

