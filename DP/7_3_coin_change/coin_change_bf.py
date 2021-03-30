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
    def coinRec(remain: int):
        nonlocal coins

        if remain == 0:
            return 0

        min_coins = float('inf')
        for coin in coins:
            if remain >= coin:
                curr_min = coinRec(remain - coin)
                min_coins = min(curr_min, min_coins)
        return min_coins + 1
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