# 30.05.2019

# Assert statement
def Function1(var1):
    assert(var1 != 5), "5 is forbidden :D"
    return 10/var1
# if assert is hit - programm is stopped
print(Function1(2))

try:
    file = open("testText.txt", "w")
    file.write("Teststring written")
except IOError:
    print("File not found")
else:
    print("everything worked finde")
    file.close()

# more stuff: https://docs.python.org/3/tutorial/errors.html