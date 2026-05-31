class Solution {
public:
    int mySqrt(int x) {
        int left = 0;
        int right = x;
        int res = 0;
        while(left <= right) {
            int mid = left + (right - left) / 2;  // 2
            if((long long) mid * mid > x) {
                right = mid - 1;
            } else if ((long long) mid * mid < x) {
                left = mid + 1;
                res = mid;
            } else {
                return mid;
            }
        }

        return res;

    }
};

// left right mid
//  0    5     2
//  3    5     4
//  3    3     3
//  3    2


// left right mid
//  0    6     3
//  0    2     1
//  2    2     2
//  3    2