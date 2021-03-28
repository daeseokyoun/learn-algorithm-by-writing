## 두 수 더하기
- Page 196
### 스택
- [add_two_num_stack.py](add_two_num_stack.py)
- Node클래스는 아래와 같이 통일합니다.
```python
class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None
```
- 책의 code에서 ```node.val```로 접근한 부분을 ```node.data```로 변경합니다.

### 연결리스트 뒤집기
- [add_two_num_revert.py](add_two_num_revert.py)
### 문자열 연산
- [add_two_num_str.py](add_two_num_str.py)
- 코드에 오기 수정합니다.
```python
...
# dummy node
>>> head = ListNode(-1)
    curr = head
...
```
- ListNode가 아니라 Node로 변경해야 합니다.

### LeetCode
- https://leetcode.com/problems/add-two-numbers-ii/
### GeeksForGeeks
- https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1






