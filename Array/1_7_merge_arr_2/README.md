## 정렬된 배열의 정합 II
- Page 70
### 수정 사항
- 코드의 변경이 있습니다.

기존 코드
```python
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for i, nums1_item in enumerate(nums1):
        if nums1_item > nums2[0]:
            nums1[i] = nums2[0]
            nums2[0] = nums1_item
            
>>>         for k, item in enumerate(nums2[1:], start=1):
>>>             if nums1_item <= item :
>>>                 nums2[k - 1] = nums1_item
>>>                 break

>>>             nums2[k - 1] = nums2[k]
```

- 두번째 for 루프 내에서 nums2의 요소 개수가 2개 이상일때, 마지막 요소가 업데이트 안되는
  문제가 있습니다.(```>>>``` 표시된 부분)
- 재 수정된 코드 참고 바랍니다.
### Brute force 방법
- [merge_arr_bf.py](merge_arr_bf.py)
### GeeksforGeeks
 - https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays/0
