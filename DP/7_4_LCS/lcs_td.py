import collections
from typing import List

tests = {
    1: ("abcde", "ace"),
    2: ("abc", "abc"),
    3: ("abc", "def")
}

res = {
    1: 3,
    2: 3,
    3: 0
}

def check_result(index: int, output: int):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return res.get(index, False) == output

def LCS(str1: str, str2: str) -> int:
    dp = [[-1 for _ in range(len(str2) + 1)] 
              for _ in range(len(str1) + 1)]

    def LCSRec(i, j):
        nonlocal str1, str2, dp

        if i >= len(str1) or j >= len(str2):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if str1[i] == str2[j]:
            dp[i][j] = 1 + LCSRec(i + 1, j + 1)
        else:
            dp[i][j] = max(LCSRec(i + 1, j),
                           LCSRec(i, j + 1))

        return dp[i][j]

    return LCSRec(0, 0)


def main():
    for index, data in tests.items():
        text1, text2 = data[0], data[1]
        res = LCS(text1, text2)

        if check_result(index, res):
            print(f'Test case {index} is correct: {res}')
        else:
            print(f'Test case {index} is failed: {res}')

if __name__ == '__main__':
    main()