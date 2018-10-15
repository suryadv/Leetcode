# Python program to find if there are
# two elements wtih given sum

# function to check for the given sum
# in the array
def printPairs(arr, arr_size, sum):

    # Create an empty hash set
    s = set()

    for i in range(0,arr_size):
        temp = sum+arr[i]
        if (temp>=0 and temp in s):
            print ("Pair with the given sum is", temp, "and", arr[i])
        s.add(arr[i])

# driver program to check the above function
A = [1,4,45,6,10,8,12]
Z = sorted(A)
Y = Z[::-1]
n = 4
printPairs(Y, len(A), n)
