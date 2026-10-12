class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        emp = {}

        for i in strs:
            key = tuple(sorted(i))

            if key not in emp:
                emp[key] = []

            emp[key].append(i)

        return list(emp.values())