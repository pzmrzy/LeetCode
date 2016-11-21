#include <math>
class Solution {
public:
    int minMoves2(vector<int>& nums) {
        nth_element(nums.begin(), nums.begin() + nums.size() / 2, nums.end());
        int mid = nums[nums.size() / 2];
        int res = 0;
        for (auto it=nums.begin(); it != nums.end(); ++it){
            res += abs(*it - mid);
        }
        return res;
    }
};
