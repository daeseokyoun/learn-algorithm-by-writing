from typing import List
import collections

tests = {
    1: ([1,2,3,4,5,6,7], 3),
    2: ([1, 2], 3)
}

res = {
    1: [5,6,7,1,2,3,4],
    2: [2, 1]
}

def is_same_list(alist: List, blist: List):
    return collections.Counter(alist) == collections.Counter(blist)

def check_result(index: int, output: List):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')

    return is_same_list(output, res.get(index, []))

def rotate(nums: List[int], k: int) -> None:
    for _ in range(k):
        prev = nums[len(nums) - 1]
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = prev
            prev = temp

def main():
    for index, data in tests.items():
        nums = data[0]
        k = data[1]
        rotate(nums, k)

        if check_result(index, nums):
            print(f'Test case {index} is correct: value {nums}')
        else:
            print(f'Test case {index} is failed: value {nums}')

if __name__ == '__main__':
    main()