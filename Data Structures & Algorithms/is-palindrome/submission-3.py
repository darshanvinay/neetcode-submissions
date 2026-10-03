class Solution:
    def isPalindrome(self, s: str) -> bool:
        flag = True
        l=0
        r= len(s)-1

        while flag and l<r:
            while not s[l].isalnum() and l < r:
                l+=1
            while not s[r].isalnum() and r > l:
                r-=1
            flag = s[l].lower() == s[r].lower()
            l+=1
            r-=1
        return flag
        
            

