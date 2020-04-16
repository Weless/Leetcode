class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0 :
            res = 1
            for _ in range(n):
                res *= x
            return res
        if n < 0 :
            res = 1
            for _ in range(-n):
                res *= 1/x
            return res