class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = list(s)
        vow = "aeiouAEIOU"
        x = [i for i in s if i in vow]
        z = x[::-1]
        v=0
        for j in range(0,len(s)):
            if string[j] in vow:
                string[j] = z[v]
                v += 1
        return(''.join(string))
