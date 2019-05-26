# 26.05.2019
# Working with LogicalOperators
# AND Operator and
# OR Operator or
# NOT Operator not

var1 = True
var2 = True
var3 = False
var4 = False

# AND Logical Operator
print(f"Logical AND Operator versions:")
print(f"Logical AND True and True: {var1 and var2}")
print(f"Logical AND True and False: {var1 and var3}")
print(f"Logical AND False and False: {var3 and var4}")
print(f"\n")

# OR Logical Operator
print(f"Logical OR Operator versions:")
print(f"Logical OR True or True: {var1 or var2}")
print(f"Logical OR True or False: {var1 or var3}")
print(f"Logical OR False or False: {var3 or var4}")
print(f"\n")

# NOT Logical Operator
print(f"Logical NOT Operator versions:")
print(f"Logical NOT not(True): {not(var1)}")
print(f"Logical NOT not(False): {not(var3)}")
print(f"Logical NOT not(True and False): {not(var1 and var3)}")
print(f"Logical NOT not(True and True): {not(var1 and var2)}")
print(f"Logical NOT not(False and False): {not(var3 and var4)}")

