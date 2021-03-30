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
    n = len(str1)
    m = len(str2)
    dp = [[-1 for _ in range(m + 1)]
           for _ in range(n + 1)]

    for i in range(m + 1):
        dp[0][i] = 0

    for j in range(n + 1):
        dp[j][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j],
                               dp[i][j - 1])
    return dp[n][m]

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