# 29.05.2019

print("Input Output Stuff")

#var1 = input("Enter something please: ")

#print(var1)
### various open modes
# 'r' open for reading (default)
# 'w' open for writing, truncating the file first 
# 'x' create a new file and open it for writing
# 'a' open for writing, appending to the end of the file if it exists
# 'b' binary mode
# 't' text mode (default)
# '+' open a disk file for updating (reading and writing)
###
var2 = open("PythonTestFile.txt","rb+")
# first 5 chars
print(var2.read(5))
# REST of the file ..
print(var2.read())

# seek resets the read postition 
# 1. value offset (where to go) .. 2. value from where to start: 0 beginning - 1 current - 2 end
var2.seek(0,0)
print(var2.read())
#negative seek only in binary mode possible
var2.seek(-5,2)
string5 = var2.read()
print("the thing \n")
    # can't get rid of the first 2 things and last things
print(str(string5))
    # but idea
print(string5[2:]) # hm - still not working

# found something
print(string5.decode('ascii')) # success!

# need to close and reopen to get the whole stream
var2.close()
var2 = open("PythonTestFile.txt","r")
print(var2.read())

# ah - blitzlicht
var2.close()
var2 = open("PythonTestFile.txt","r+")
# read everything to a string var to manipulate it
# do not goof around inside the open file .. probably
stringwithcontent = var2.read()

#print(stringwithcontent[2:10])
#print(stringwithcontent[4:6])
stringwithcontent += " do crazy stuff"
#print(stringwithcontent)


# flushing
var2.close()