class Solution {
public:
    bool isPowerOfThree(int n) {
        double t1 = log(n) / log(3);
        double diff = t1 - round(t1);
        if (fabs(diff) < 0.0000000001 )
            return true;
        else
            return false;
    }
};
