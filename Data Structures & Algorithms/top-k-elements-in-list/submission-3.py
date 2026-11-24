class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        emp={}

        for i in nums:
            if i not in emp:
                emp[i]=1
            else:
                emp[i]+=1
        
        w=sorted(emp, key=emp.get, reverse=True)

        return w[:k]