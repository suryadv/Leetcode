def printPairs(arr, arr_size, sum):

    # Create an empty hash set
    s = set()

    for i in range(0,arr_size):
        temp = sum/arr[i]
        if (temp>=0 and temp in s):
            print ("Pair with the given product is", int(temp), "and", arr[i])
        s.add(arr[i])

# driver program to check the above function
A = [2,4,45,16,10,8,12]
Z = sorted(A)
n = 32
printPairs(Z, len(A), n)
