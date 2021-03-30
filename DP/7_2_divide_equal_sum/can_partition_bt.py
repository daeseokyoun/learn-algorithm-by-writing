import collections
from typing import List

tests = {
    1: [1,5,11,5],
    2: [1,2,3,5],
    3: [1, 1, 5, 7],
    4: [1, 2, 5],
    5: [1, 4, 5]
}

res = {
    1: True,
    2: False,
    3: True,
    4: False,
    5: True 
}

def check_result(index: int, output: bool):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return res.get(index, -1) == output

def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    n = len(nums)
    if total % 2 != 0:
        return False

    half = int(total/2)
    dp = [[False for x in range(half+1)]
              for y in range(n)]

    for i in range(n):
        dp[i][0] = True

    for s in range(half + 1):
        if nums[0] == s:
            dp[0][s] = True

    for i in range(1, n):
        for s in range(1, half + 1):
            if dp[i - 1][s]:
                dp[i][s] = dp[i - 1][s]
            elif s >= nums[i]:
                dp[i][s] = dp[i - 1][s - nums[i]]

    return dp[n - 1][half]

def main():
    for index, input_list in tests.items():
        res = canPartition(input_list)

        if check_result(index, res):
            print(f'Test case {index} is correct: {res}')
        else:
            print(f'Test case {index} is failed: {res}')

if __name__ == '__main__':
    main()
