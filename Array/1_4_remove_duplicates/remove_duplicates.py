from typing import List

tests = {
    1: [],
    2: [1, 2, 3, 4],
    3: [0, 0, 1, 1, 1, 2]
}

res = {
    1: 0,
    2: 4,
    3: 3
}

def check_result(index: int, output: int):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return bool(output == res.get(index, -1))

def removeDuplicates(nums: List[int]) -> int:    
    if len(nums) <= 0:
        return 0

    curr = nums[0]
    cnt = 1

    for i in range(1, len(nums)):
        if curr != nums[i]:
            curr = nums[i]
            nums[cnt] = curr
            cnt += 1

    return cnt

def main():
    for index, input_list in tests.items():
        count = removeDuplicates(input_list)

        if check_result(index, count):
            print(f'The duplicate count in input list {input_list} is ', end='')
            print(f'{count}')
        else:
            print(f'wrong duplicate count {count}')

if __name__ == '__main__':
    main()