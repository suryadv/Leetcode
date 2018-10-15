n = [10,20,30,40,50,60]
k = 70
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        if n[i]+n[j]<=k:
            print(n[i],n[j])
