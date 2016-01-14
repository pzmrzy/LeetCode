class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int, int> mapint;
        for (auto it = nums.begin(); it != nums.end(); ++it){
            mapint[*it]++;
        }
        int result = 0, resnum = 0;
        for (auto it = mapint.begin(); it != mapint.end(); ++it){
            if (it->second > resnum){
                resnum = it->second;
                result = it->first;
            }
        }
        return result;
    }
};
