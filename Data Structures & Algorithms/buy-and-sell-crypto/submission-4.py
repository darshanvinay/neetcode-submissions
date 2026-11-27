class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        l=0
        r=l+1

      
        while r<=len(prices)-1:
            if prices[r]<prices[l]:
                l=r
                
            else:
                maxi= max(maxi, prices[r]-prices[l])
            r+=1
        
        return maxi