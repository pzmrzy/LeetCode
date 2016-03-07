class Solution {
public:
    int trailingZeroes(int n) {
        int p = 5;
        int result = 0;
        while (n > 0){
            result += n / p;
            n /= 5;
        }
        return result;
    }
};
