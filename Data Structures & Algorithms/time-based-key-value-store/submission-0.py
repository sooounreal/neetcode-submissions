class TimeMap:

    def __init__(self):
        self.kv = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kv:
            self.kv[key].append((timestamp, value))
        else:
            self.kv[key] = [(timestamp,value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""
        
        # binary search
        values = self.kv[key]
        right = len(values)
        left = 0
        while left < right:
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1
        
        if values[mid][0] < timestamp:
            return values[mid][1]
        elif mid > 0:
            return values[mid-1][1]
        else:
            return ""