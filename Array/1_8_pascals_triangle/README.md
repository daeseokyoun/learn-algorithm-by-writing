## 파스칼의 삼각형
- Page 76
### Brute force 방법
- [pascal_triangle.py](pascal_triangle.py)
### 오타 수정
```python
    for i in range(1, numRows):
        prev_len = len(pascal[i - 1])
        curr_list = []

>>>     for j in range(prev_level_len + 1):
            num = 1
            if j != 0 and j != prev_len:
```
- 표시된 라인에 ```prev_level_len```을 ```prev_len```으로 정정합니다.

### Hackerrank
 - 파스칼의 삼각형 https://www.hackerrank.com/challenges/pascals-triangle/problem
### LeetCode
 - 파스칼의 삼각형 https://leetcode.com/problems/pascals-triangle/
