"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A,
followed by all the odd elements of A

"""

def sortparity(A):
    l = []
    l1 = []
    for x in A:
        if x %2 == 0:
            l.append(x)
        else:
            l1.append(x)
    return l+l1


a = [4,1,3,2]
z = sortparity(a)
print(z)
