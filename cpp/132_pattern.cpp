class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        if (n <= 2)
            return false;
        int i = 0, j = 0, k = 0;
        while (i < n){
            while ((i + 1 < n) && (nums[i + 1] <= nums[i]))
                i++;
            j = i + 1;
            while ((j + 1 < n) && (nums[j + 1] >= nums[j]))
                j++;
            k = j + 1;
            while (k < n){
                if ((nums[i] < nums[k]) and (nums[k] < nums[j]))
                    return true;
                k++;
            }
            i = j + 1;
        }
        return false;
    }
};
