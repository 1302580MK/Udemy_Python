# 27.05.2019

# more depth to lists and how to use them

listNumber1 = [1, 2, 3, 4, 5, "Hello", "Marc", 6,7]

#Access
print(listNumber1)
print(listNumber1[2])
print(listNumber1[2:])

#Update

listNumber1[0]="bob"
print(listNumber1)

#delete

del listNumber1[2]
print(listNumber1)

#len

print(len(listNumber1))
