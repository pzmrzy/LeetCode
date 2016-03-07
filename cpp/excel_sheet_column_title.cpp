class Solution {
public:
    string convertToTitle(int n) {
        string s = "";
        while (n > 0){
            int t = n % 26;
            if (t == 0){
                t = 26;
                n -= 26;
            }
            char c = 'A' + t - 1;
            s = c + s;
            n /= 26;
        }
        return s;
    }
};
