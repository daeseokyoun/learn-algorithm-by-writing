from typing import List

tests = {
    1: 2,
    2: 3,
    3: 4,
}

res = {
    1: 2,
    2: 3,
    3: 5,
}

def check_result(index: int, output: int):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return res.get(index, -1) == output

def climbStairs(n: int) -> int:
    def climb(n, i):
        if n == i:
           return 1
        if n < i:
           return 0
            
        return climb(n, i + 1) + climb(n, i + 2)
        
    return climb(n, 0)

def main():
    for index, input_val in tests.items():
        res = climbStairs(input_val)

        if check_result(index, res):
            print(f'Test case {index} is correct: value {res}')
        else:
            print(f'Test case {index} is failed: value {res}')

if __name__ == '__main__':
    main()