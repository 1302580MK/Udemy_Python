tupel = (1,2,3,4,5,"a","b")

print(tupel)
print(tupel[1])
print(tupel[0:4])

print(len(tupel))
del tupel[1] # not working
del tupel
print(tupel) # is now deleted