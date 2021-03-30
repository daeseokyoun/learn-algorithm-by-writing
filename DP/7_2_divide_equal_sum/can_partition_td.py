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
    return res.get(index, False) == output

def canPartition(nums: List[int]) -> bool:
    s = sum(nums)
    if s % 2 != 0:
        return False

    def canPartitionRec(dp: List[int], nums: List[int],
                        s, index):
        if s == 0:
            return 1
        if index >= len(nums):
            return 0

        if dp[index][s] == -1 and nums[index] <= s:
            if canPartitionRec(dp, nums,
                 s - nums[index], index + 1) == 1:
                dp[index][s] = 1
                return 1

        dp[index][s] = canPartitionRec(dp, nums, s,
                                       index + 1)
        return dp[index][s]

    dp = [[-1 for x in range(int(s/2)+1)]
           for y in range(len(nums))]
    return True if canPartitionRec(dp, nums, int(s/2),
                                   0) == 1 else False

def main():
    for index, input_list in tests.items():
        res = canPartition(input_list)

        if check_result(index, res):
            print(f'Test case {index} is correct: {res}')
        else:
            print(f'Test case {index} is failed: {res}')

if __name__ == '__main__':
    main()
