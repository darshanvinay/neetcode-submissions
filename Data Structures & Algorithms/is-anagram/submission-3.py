class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict={}
        mydict2={}
        if not len(s)==len(t):
            return False
        for i in range(len(s)):
            if s[i] in mydict:
                mydict[s[i]]+=1
            else: 
                mydict[s[i]]= 1
            if t[i] in mydict2:
                mydict2[t[i]]+=1
            else: 
                mydict2[t[i]]= 1
        if mydict == mydict2:
            return True
        else:
            return False

