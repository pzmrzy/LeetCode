class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int count = 0;
        for (auto it = nums.begin(); it != nums.end(); ++it){
            if (*it == 0){
                nums.erase(it);
                --it;
                count++;
            }
        }
        for (int i=0; i<count; i++){
            nums.push_back(0);
        }
    }
};

