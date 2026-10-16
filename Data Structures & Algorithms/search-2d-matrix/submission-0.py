class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        h1=0
        h2=len(matrix)-1
        m=len(matrix[0])

        while h1<=h2:
            mid= (h1+h2)//2
            if target< matrix[mid][0]:
                h2=mid-1
            
            elif target> matrix[mid][m-1]:
                h1=mid+1

            else:
                l=0
                r=m-1
                
                while l<=r:
                    mid2=(l+r)//2
                    if target<matrix[mid][mid2]:
                        r=mid2-1
                    elif target>matrix[mid][mid2]:
                        l=mid2+1
                    else:
                        return True
                return False
        return False