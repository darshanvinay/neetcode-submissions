class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        l=-1

        for i in range(len(prices)):
            l+=1
            r=l+1
            while r<=len(prices)-1:
                maxi= max(maxi, prices[r]-prices[l])
                r+=1
        return maxi

        
