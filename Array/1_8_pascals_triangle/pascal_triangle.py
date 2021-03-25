from typing import List

tests = {
    1: 5,
    2: 0,
    3: 1
}

res = {
    1: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]],
    2: [],
    3: [[1]]
}

def is_same_2d_list(alist: List, blist: List):
    return any(
        aitem and bitem
        for arow, brow in zip(alist, blist)
        for aitem, bitem in zip(arow, brow)
    ) or (not blist)

def check_result(index: int, output: List):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')

    return is_same_2d_list(output, res.get(index, []))

def generate(numRows: int) -> List[List[int]]:
    pascal = []

    if numRows <= 0:
        return pascal

    pascal.append([1])

    for i in range(1, numRows):
        prev_len = len(pascal[i - 1])
        curr_list = []

        for j in range(prev_len + 1):
            num = 1
            if j != 0 and j != prev_len:
                num = pascal[i - 1][j - 1] + pascal[i - 1][j]
            curr_list.append(num)

        pascal.append(curr_list)

    return pascal

def main():
    for index, num_rows in tests.items():
        output = generate(num_rows)

        if check_result(index, output):
            print(f'Test case {index} is correct: value {output}')
        else:
            print(f'Test case {index} is failed: value {output}')

if __name__ == '__main__':
    main()