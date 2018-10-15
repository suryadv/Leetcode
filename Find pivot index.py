z = [1,7,3,6,5,6]
l1 = 0
total = sum(z)
for i in range(len(z)):
    if l1 == total-l1 - z[i]:
        print(i)
    l1 += z[i]
