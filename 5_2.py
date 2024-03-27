a=[1,2,3,45,4,3,21,1]
for i in (0,len(a)-1):
    for x in (0,len(a)-1):
        if a[i] == a[x]:
            print(a[x])
            break
