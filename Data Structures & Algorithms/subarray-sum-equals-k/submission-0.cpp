class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int res = 0;
        for(int i=0; i<nums.size(); i++){
            int cursum = 0;
            for(int j=i; j<nums.size(); j++){
                cursum = cursum + nums[j];
                if(cursum == k){
                    res ++;
                }
            }
        }

        return res;
    }
};