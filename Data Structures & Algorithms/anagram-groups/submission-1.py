class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        emp={}
        
        for str in strs:
            key= tuple(sorted(str))
       
            if key not in emp:
                emp[key]= []
            
            emp[key].append(str)

        return list(emp.values())
