class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            maxi=0
            l=0
            arr={}

            for i in range(len(s)):
                if s[i] in arr:
                    arr[s[i]]+=1
                else: 
                    arr[s[i]]=1
            

                while (i-l+1) - max(arr.values())>k:
                    arr[s[l]]-=1
                    l+=1

                maxi= max(maxi, (i-l+1))
            return maxi

            