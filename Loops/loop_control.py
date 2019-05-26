# 26.05.2019
# loop control - continue, break, pass

var1 = "Hello World"

for character in var1:
    if(character == ' '):
        print("there was a space - i'll break out")
        break # break out
    print(character)

for character in var1:
    if(character == ' '):
        print("there was a space - i will not print it and continue")
        continue # continue and skip this iteration
    print(character)

for character in var1:
    if(character == ' '):
        print("passing - i will do it, but here is something to care about")
        pass # passing this over
    print(character)