from typing import List
import sys

import heapq

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
    prio_queue = [item * -1 for item in
                  list(dict.fromkeys(nums))]
    heapq.heapify(prio_queue)

    if len(prio_queue) > 2:
        cnt = 2

        while cnt > 0:
            heapq.heappop(prio_queue)
            cnt -= 1

    return prio_queue[0] * -1

def main():
    for index, input_list in tests.items():
        res = thirdMax(input_list)

        if check_result(index, res):
            print(f'Test case {index} is correct: value {res}')
        else:
            print(f'Test case {index} is failed: value {res}')

if __name__ == '__main__':
    main()