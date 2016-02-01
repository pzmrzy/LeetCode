class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if (nums.size() == 0) return false;
        bool result = false;
        sort(nums.begin(), nums.end());
        for (auto it=nums.begin(); it!=nums.end()-1;){
            if (*it == *++it){
                result = true;
                break;
            }
        }
        cout << result;
        return result;
    }
};

