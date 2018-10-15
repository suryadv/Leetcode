class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <10:
            return num
        else:
            list = [int(i) for i in str(num)]
            return self.addDigits(sum(list))
