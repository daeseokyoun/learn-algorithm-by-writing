import collections
from typing import List

tests = {
    1: ([1,2,5], 11),
    2: ([2], 3),
    3: ([1], 0),
    4: ([1], 1),
    5: ([1], 2)
}

res = {
    1: 3,
    2: -1,
    3: 0,
    4: 1,
    5: 2
}

def check_result(index: int, output: int):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return res.get(index, False) == output

def coinChange(coins: List[int], amount: int) -> int:
    dp = [-1 for _ in range(amount + 1)]

    def coinRec(remain: int):
        nonlocal dp, coins
        if remain == 0:
            return 0

        if dp[remain] != -1:
            return dp[remain]

        min_coin = float('inf')
        for coin in coins:
            if remain >= coin:
                min_coin = min(min_coin, 
                           coinRec(remain - coin) + 1)
        dp[remain] = min_coin
        return dp[remain]
    res = coinRec(amount)
    return res if res != float('inf') else -1

def main():
    for index, data in tests.items():
        coins, amount = data[0], data[1]
        res = coinChange(coins, amount)

        if check_result(index, res):
            print(f'Test case {index} is correct: {res}')
        else:
            print(f'Test case {index} is failed: {res}')

if __name__ == '__main__':
    main()