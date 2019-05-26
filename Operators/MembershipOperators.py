# 26.05.2019
# Membership Operators 'in' and 'not in' to check if for example is the letter a in the string Marc
string1 = "Hello Marc"

print(f"Evaluating if a certain letter is inside a string with the membership operators 'in' and 'not in'")

# in
print(f"Hello Marc beinhaltet ein a: {'a' in string1}")
print(f"Hello Marc beinhaltet kein x: {'x' in string1}")

print(f"Learning: Ich brauche einen Char 'x' damit 'x' in string1 funktioniert doppelte Anfürhungszeichen haben nicht geklappt. ")

# not in
print(f"Trying not in")
print(f"Hello Marc beinhaltet ein a: {'a' not in string1}")
print(f"Hello Marc beinhaltet kein x : {'x' not in string1}")
print(f"\n")

# does it work with arrays?

# Learning: Arrays are called Lists in Python :D

print(f"trying the same thing with a list of [1, 2, 3]")
var3 = [1,2,3]

print(f"[1, 2, 3] beinhaltet eine 1: {1 in var3}")
print(f"[1, 2, 3] beinhaltet eine 6: {6 in var3}")
print(f"[1, 2, 3] beinhaltet eine 3: {3 in var3}")
