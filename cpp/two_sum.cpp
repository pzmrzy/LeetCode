#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int l, r;
        bool flag = false;
        for (int i = 0; i < nums.size(); i++){
            for (int j = i + 1; j < nums.size(); j++)
                if (nums[i] + nums[j] == target){
                    l = i; r = j;
                    flag = true;
                    break;
                }
            if (flag)
                break;
        }

        vector<int> result = {l + 1, r + 1};
        return result;
    }
};

