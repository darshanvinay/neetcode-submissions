class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        l=0
        r=0

        maxLeft= [0]*n
        maxRight =[0]*n

        for i in range(n):
            j= -i -1
            maxLeft[i]= l
            maxRight[j]= r
            l= max(maxLeft[i], height[i])
            r= max(maxRight[j], height[j])

        sum=0

        for i in range(n):
            pot= min( maxLeft[i], maxRight[i])
            sum+= max(0, pot-height[i])
        return sum



        