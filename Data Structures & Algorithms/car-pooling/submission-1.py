class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        for t in trips:
            if t[0] > capacity:
                return False
        
        sorted_trips = [(t[1],t[2],t[0]) for t in trips]
        sorted_trips.sort()
        print(sorted_trips)

        # merge the trips
        merged_trips = []
        prev_trip = sorted_trips[0]
        for i in range(1, len(sorted_trips)):
            trip = sorted_trips[i]
            if prev_trip[1] > trip[0]:
                # merge
                if prev_trip[2] + trip[2] > capacity:
                    return False
                prev_trip = (prev_trip[0], trip[1], prev_trip[2] + trip[2])
                
            else:
                prev_trip = trip
        return True
        

