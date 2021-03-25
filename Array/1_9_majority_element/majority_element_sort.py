from typing import List

tests = {
    1: [1],
    2: [3,2,3],
    3: [2,2,1,1,1,2,2] 
}

res = {
    1: 1,
    2: 3,
    3: 2
}

def check_result(index: int, output: int):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return output == res.get(index, -1)

def majorityElement(nums: List[int]) -> int:
    return sorted(nums)[int(len(nums)/2)]

def main():
    for index, input_list in tests.items():
        output = majorityElement(input_list)

        if check_result(index, output):
            print(f'Test case {index} is correct: value {output}')
        else:
            print(f'Test case {index} is failed: value {output}')

if __name__ == '__main__':
    main()