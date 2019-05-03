class Solution:
    def myPow(self, x, n):
        '''
        :param x: float
        :param n: int
        :return: float
        '''
        #return x ** n

        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        #　execute when n is even
        return self.myPow(x*x, n/2)


# test
x = 2.10000
n = 3
print(Solution().myPow(x, n))

