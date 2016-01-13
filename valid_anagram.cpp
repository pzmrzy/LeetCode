class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        int result = s.compare(t);
        return result==0? true:false;
//        cout << s << " " << t << " " << s.compare(t) << endl;
//        
//        int a[26], b[26];
//        for (int i=0; i<26; i++){
//            a[i] = 0;
//            b[i] = 0;
//        }
//        for (auto ch = s.begin(); ch != s.end(); ++ch){
//            a[*ch-'a']++;
//        }
//        for (auto ch = t.begin(); ch != t.end(); ++ch){
//            b[*ch-'a']++;
//        }
//        bool result = true;
//        for (int i=0; i<26; i++){
//            if (a[i] != b[i]){
//                result = false;
//                break;
//            }
//        }
//        cout << result;
//        return result;
    }
};
