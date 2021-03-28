from typing import List
import sys

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
    5: 2,
}

def check_result(index: int, output: int):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return res.get(index, -1) == output

def coinChange(coins: List[int], value: int) -> int:
    def change(v:int):
        if v == 0:
            return 0

        min_coin_cnt = sys.maxsize
        for c in coins:
            if (v - c) >= 0:
                change_cnt = change(v - c)
                if change_cnt < min_coin_cnt:
                    min_coin_cnt = change_cnt

        return min_coin_cnt + 1

    ans = change(value)

    return ans if ans != sys.maxsize + 1 else -1

def main():
    for index, data in tests.items():
        coins = data[0]
        value = data[1]
        res = coinChange(coins, value)

        if check_result(index, res):
            print(f'Test case {index} is correct: value {res}')
        else:
            print(f'Test case {index} is failed: value {res}')

if __name__ == '__main__':
    main()