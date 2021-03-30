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
    if sum(nums) % 2 != 0:
        return False

    def canPartitionRec(nums: List[int], s, index):
        if s == 0:
            return True
        if index >= len(nums):
            return False

        if s - nums[index] >= 0:
            if canPartitionRec(nums, s - nums[index],
                               index + 1):
                return True
        return canPartitionRec(nums, s, index + 1)

    return canPartitionRec(nums, int(sum(nums)/2), 0)

def main():
    for index, input_list in tests.items():
        res = canPartition(input_list)

        if check_result(index, res):
            print(f'Test case {index} is correct: {res}')
        else:
            print(f'Test case {index} is failed: {res}')

if __name__ == '__main__':
    main()
