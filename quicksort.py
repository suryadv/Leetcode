arr = [3,5,4,1,6]
len1 = len(arr)
len2= int(len1/2)
x = arr[len2]
y = [x]
#print(x)
a1 = []
a2 = []
for i in arr:
    if i < x:
        a1.append(i)
for j in arr:
    if j > x:
        a2.append(j)

print(a1)
print(a2)
farr = a1+y+a2
print(farr)
