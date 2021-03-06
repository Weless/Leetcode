from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(A[0])):
            res.append([])
            for j in range(len(A)):
                res[i].append(A[j][i])
        return res

s = Solution()
A = [[1,2,3],[4,5,6]]
print(s.transpose(A))