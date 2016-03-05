class NumArray {
public:
    vector<int> partsums;
    NumArray(vector<int> &nums) {
        partsums.push_back(0);
        for (auto i=0; i<nums.size(); ++i){
            partsums.push_back(nums[i] + partsums.back());
        }
    }

    int sumRange(int i, int j) {
        return partsums[j + 1] - partsums[i];
    }
};

