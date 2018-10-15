class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        b,c,d = 0,0,0
        for x,y in enumerate(nums):
            b,c,d = c,d,max(b+y,c+y)
        return(max(c,d))
