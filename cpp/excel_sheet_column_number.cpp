class Solution {
public:
    int tonum(char s){
        return s - 'A' + 1;
    }
    int titleToNumber(string s) {
        int result = tonum(s[0]);
        for (auto it = s.begin()+1; it < s.end(); ++it){
            result = result * 26 + tonum(*it);
        }
        return result;
    }
};
