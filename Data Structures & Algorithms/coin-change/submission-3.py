class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins = [1,5,10], amount = 12
        # i = 0
        # coins [5,2], amount = 16
        # 1. 16 - 5 = 11 i = 0
        # 2. 1 - 2 = -1 if i == len(coins) - 1 and amount - coins[i] < 0 return -1
        # choice(1: i+1, amount - coins[i], 2: i, amount - coins[i])

        # coins=[2]
        #.  amount=3
        memo = defaultdict(lambda: 2**31-1 )
        def dfs(currAmt):
            # if currAmt < 0:
            #     return 2**31 - 1
            if currAmt == 0:
                return 0
            if currAmt in memo:
                return memo[currAmt]
            
            for coin in coins:
                if currAmt - coin >= 0:
                    memo[currAmt] = min(memo[currAmt], dfs(currAmt - coin))
    
            memo[currAmt] += 1

            return memo[currAmt]
        res = dfs(amount)
        return -1 if res > 10000 else res

        