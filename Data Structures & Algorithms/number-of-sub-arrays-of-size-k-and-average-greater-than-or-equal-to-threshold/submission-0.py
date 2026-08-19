class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        right = k-1
        cur_sum = sum(arr[left:right])

        res = 0
        while right < len(arr):
            cur_sum += arr[right]
            print(left, cur_sum/k)
            if cur_sum / k >= threshold:
                res += 1
            cur_sum -= arr[left]
            left += 1
            right += 1
        return res

