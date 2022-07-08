tup=(5,3,0,7,4,1,6,2)
for i in range(0,len(tup)):
    for j in range(i+1,len(tup)):
        if tup[i] >= tup[j]:
            temp = tup[i]
            tup[i] = tup[j]
            tup[j] =temp

print(tup)