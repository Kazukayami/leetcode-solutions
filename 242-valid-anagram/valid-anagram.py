class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1={}
        dict2={}
        if len(s)==len(t):
            for i in range(len(s)):
                dict1[s[i]]= dict1.get(s[i],0)+1
                dict2[t[i]]= dict2.get(t[i],0)+1
            return dict1==dict2
        else:
            return False
        