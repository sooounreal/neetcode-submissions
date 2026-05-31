class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search

        left = 0
        right = len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == x:
                break
            elif arr[mid] > x:
                right = mid - 1
            else:
                left = mid + 1
        res = []
        if arr[mid] == x:
            res.append(arr[mid])
            left = mid - 1
            right = mid + 1
        elif arr[mid] < x:
            left = mid
            right = mid + 1
        else:
            left = mid - 1
            right = mid
        
        while len(res) < k:
            if left < 0:
                for i in range(k-len(res)):
                    res.append(arr[right+i])
                break
            elif right >= len(arr):
                for i in range(k-len(res)):
                    res.append(arr[left-i])
                break
            
            if abs(x - arr[left]) <= abs(x-arr[right]):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
        return sorted(res)
        