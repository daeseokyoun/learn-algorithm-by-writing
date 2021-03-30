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

def check_result(index: int, output: bool):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return res.get(index, False) == output

def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf') for _ in range(amount + 1)]

    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i - c] + 1, dp[i])

    return dp[amount]

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