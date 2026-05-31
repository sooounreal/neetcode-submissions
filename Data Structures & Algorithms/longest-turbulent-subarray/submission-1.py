class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        cur_max = 1
        cur_sign = None
        global_max = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:  # same value - ends here
                cur_max = 1
                cur_sign = None
            elif not cur_sign:  # reset 
                cur_sign = 1 if arr[i] > arr[i-1] else -1
                cur_max += 1
            elif (arr[i] - arr[i-1]) * cur_sign > 0:  # -- this needs to be fixed, can reset to 2
                if arr[i] == arr[i-1]:
                    cur_max = 1
                    cur_sign = None
                else:
                    cur_max = 2
                    cur_sign = 1 if arr[i] > arr[i-1] else -1
            else:
                cur_max += 1
                cur_sign *= -1
            print(arr[i], cur_sign, cur_max)
            global_max = max(global_max, cur_max)
        return global_max