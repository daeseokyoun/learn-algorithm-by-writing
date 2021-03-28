from typing import List

tests = {
    1: [1,2,3],
    2: [0]
}

res = {
    1: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]],
    2: [[],[0]]
}

def is_same_2d_list(alist: List, blist: List):
    a_set = set(map(tuple, alist))
    b_set = set(map(tuple, blist))

    return a_set == b_set

def check_result(index: int, output: List):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')

    return is_same_2d_list(output, res.get(index, []))

def subsets_recursion(nums: List[int],
    res: List[List[int]], sub: List[int],
    index) -> None:
    if len(sub) > len(nums):
        return

    res.append(sub.copy())

    for i in range(index, len(nums)):
        sub.append(nums[i])
        subsets_recursion(nums, res, sub, i + 1)
        sub.pop()

def main():
    for index, input_list in tests.items():
        output = []
        subsets_recursion(input_list, output, [], 0)

        if check_result(index, output):
            print(f'Test case {index} is correct: value {output}')
        else:
            print(f'Test case {index} is failed: value {output}')

if __name__ == '__main__':
    main()