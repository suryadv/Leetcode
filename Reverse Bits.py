class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rev="{0:032b}".format(n)
        rev=rev[::-1]
        return int(rev,2)
