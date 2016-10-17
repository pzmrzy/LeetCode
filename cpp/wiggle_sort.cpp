#include<algorithm>
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        if (nums.size() == 0)
            return;
        nth_element(nums.begin(), nums.begin() + nums.size() / 2, nums.end());
        int mid = nums[nums.size() / 2];
        vector<int> small;
        vector<int> large;
        int nmid = 0;
        for (int i=0; i<nums.size(); i++){
            if (nums[i] > mid)
                large.push_back(nums[i]);
            else if (nums[i] < mid)
                small.push_back(nums[i]);
            else
                nmid += 1;
        }
        if (large.size() < small.size()){
            int t = small.size() - large.size();
            for (int i=0; i<t; i++)
                large.push_back(mid);
            nmid -= t;
        }else if (large.size() > small.size()){
            int t = large.size() - small.size();
            for (int i=0; i<t; i++)
                small.push_back(mid);
            nmid -= t;
        }
        int t = nmid / 2;
        for (int i=0; i<t; i++)
            large.push_back(mid);
        nmid -= t;
        for (int i=0; i<nmid; i++)
            small.push_back(mid);
        
        int nl = 0;
        int ns = 0;
        for (int i=0; i<nums.size(); i++){
            if (i % 2 == 0){
                nums[i] = small[nl++];
            }else
                nums[i] = large[ns++];
        }
    }
};
