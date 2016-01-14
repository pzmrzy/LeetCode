class Solution {
public:
    int climbStairs(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 2;
        int a1 = 1;
        int a2 = 2;
        int t = 0;
        for (int i=3; i <= n; i++){
            a1 = a1 + a2;
            t = a1;
            a1 = a2;
            a2 = t;
        }
        return a2;
    }
};
