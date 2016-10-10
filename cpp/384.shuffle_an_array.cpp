class Solution {
vector<int> s;
vector<int> r;
int n;
public:
    Solution(vector<int> nums) {
        srand(time(NULL));
        s = vector<int>(nums);
        r = vector<int>(nums);
        n = s.size();
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        // s = vector<int>(r);
        return r;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        for (int i=n-1; i>0; i--) {
            int j = rand() % (i + 1);
            swap(s[i], s[j]);
         }
         return s;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */
