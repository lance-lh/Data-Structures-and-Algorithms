'''
You are given coins of different denominations
and a total amount of money amount.
Write a function to compute the fewest number of coins
that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

    Input: coins = [1, 2, 5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
Example 2:

    Input: coins = [2], amount = 3
    Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''


class Solution:
    def coinChange(self, coins, amount):
        '''
        :param coins: List[int]
        :param amount: int
        :return: int
        '''
        # set impossible value
        MAX = float('inf')
        dp = [0] + amount * [MAX]

        # amount
        for i in range(1, amount + 1):
            # coins of different denominations
            for j in range(len(coins)):
                # each time, compare amount > value of coins
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        # if (min num of coins) <= amount, return dp[-1]
        # if (min num of coins) >  amount, in this case, we have to say it's impossible!
        return -1 if amount < dp[-1] else dp[-1]

# test
coins = [1, 2, 5]
amount = 11
print(Solution().coinChange(coins,amount))