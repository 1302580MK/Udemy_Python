# 26.05.2019

# if statements

var1 = 500
var2 = 400
var3 = 500

if(var1 == var3):
    print("No")

if(var1 == var2):
    print("Yes")
else: 
    print("Else Statement")

# combine if statements

if(var1 == 200):
    print ("test")
elif(var1  == 500):
    print("you did it")
else: # sowas wie default bei switch, wenn nichts zutrifft.
    print("bum")