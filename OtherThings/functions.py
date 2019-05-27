# 27.05.2019


# functions


def AwesomeFunction():
    "This function does stuff"
    print("Marc ist toll")
    return



AwesomeFunction()

def Funtion2(number1, number2):
    "adds numbers"
    return number1 + number2

print(Funtion2(2,5))

var1 =5
print(var1)

def ChangeFunction(number1):
    var1 = 8  # kein Zugriff
    return var1

print(ChangeFunction(var1))
print(var1)

def DefaultArg(var1 = 10):
    return var1 *2

print(var1)
print(DefaultArg())
print(DefaultArg(2))