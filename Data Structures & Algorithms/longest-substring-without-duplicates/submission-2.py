class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset=set()
        l=0
        maxLen=0

        for i in range(len(s)):
            while s[i] in myset:
                myset.remove(s[l])
                l+=1
            myset.add(s[i])
            maxLen=max(maxLen, i+1-l)
        return maxLen




                
