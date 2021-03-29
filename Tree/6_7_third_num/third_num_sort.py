from typing import List
import sys

tests = {
    1: [3, 2, 1],
    2: [1,2],
    3: [2,2,3,1],
    4: [2, 3, 2, 3, 4, 5, 1, 1, 1],
    5: [1,1,1,1,1,4,4,4]
}

res = {
    1: 1,
    2: 2,
    3: 1,
    4: 3,
    5: 4,
}

def check_result(index: int, output: int):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return res.get(index, -1) == output

def thirdMax(nums: List[int]) -> int:
    cnt = 0
    third_max = 0

    check_dup = set()

    nums.sort(reverse=True)
    third_max = nums[0]

    for num in nums:
        if num in check_dup:
            continue

        check_dup.add(num)

        if cnt == 2:
            third_max = num
            break

        cnt += 1

    return third_max

def main():
    for index, input_list in tests.items():
        res = thirdMax(input_list)

        if check_result(index, res):
            print(f'Test case {index} is correct: value {res}')
        else:
            print(f'Test case {index} is failed: value {res}')

if __name__ == '__main__':
    main()