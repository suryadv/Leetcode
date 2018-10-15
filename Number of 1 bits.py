class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin1 = str(bin(n)[2:])
        list1 = [i for i in bin1 if i == '1']
        return len(list1)

