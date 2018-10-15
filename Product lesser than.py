def fun(A, k):
    # count to keep count of number
    # of pairs with product less than k
    count = 0
    n = len(A)
    # Left pointer pointing to leftmost part
    i = 0

    # Right pointer pointing to rightmost part
    j = n-1

    # While left and right pointer don't meet
    while i < j:
        if A[i]*A[j] < k:
            count += (j-i)
            # Increment the left pointer
            i+= 1
        else:
            # Decrement the right pointer
            j-= 1
    return count

# Driver code to test above function
A = [2, 3, 4, 6, 9]
k = 20
print("Number of pairs with product less than ", k, " = ", fun(A, k))
