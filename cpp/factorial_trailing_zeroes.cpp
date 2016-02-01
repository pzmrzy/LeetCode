class Solution {
public:
    int trailingZeroes(int n) {
        int p = 5;
        int result = 0;
        while (p < n){
            result += n / p;
            p *= 5;
        }
        return result
    }
};
